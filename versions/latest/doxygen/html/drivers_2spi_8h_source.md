---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2spi_8h_source.html
original_path: doxygen/html/drivers_2spi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <stddef.h>

24#include <[zephyr/device.h](device_8h.md)>

25#include <[zephyr/dt-bindings/spi/spi.h](dt-bindings_2spi_2spi_8h.md)>

26#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

27#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

28#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

29#include <[zephyr/rtio/rtio.h](rtio_8h.md)>

30#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 40](group__spi__interface.md#ga5b9d40fa0f455b1e63f8040b3316b0da)#define SPI\_OP\_MODE\_MASTER 0U

[ 41](group__spi__interface.md#ga1c3310d3711cb99cdb78fa9d1c970779)#define SPI\_OP\_MODE\_SLAVE BIT(0)

43#define SPI\_OP\_MODE\_MASK 0x1U

[ 46](group__spi__interface.md#ga6dd4395e027407a7b3b92cff2abcc8b3)#define SPI\_OP\_MODE\_GET(\_operation\_) ((\_operation\_) & SPI\_OP\_MODE\_MASK)

48

53

[ 59](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)#define SPI\_MODE\_CPOL BIT(1)

60

[ 68](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)#define SPI\_MODE\_CPHA BIT(2)

69

[ 75](group__spi__interface.md#ga8619b297de563eca6852af34c79daa62)#define SPI\_MODE\_LOOP BIT(3)

77#define SPI\_MODE\_MASK (0xEU)

[ 80](group__spi__interface.md#gaa3582b96ff42dba0b0ad815c727d5e42)#define SPI\_MODE\_GET(\_mode\_) \

81 ((\_mode\_) & SPI\_MODE\_MASK)

82

84

[ 89](group__spi__interface.md#ga7761f42c6241cf396fc02d0de8617e46)#define SPI\_TRANSFER\_MSB (0U)

[ 90](group__spi__interface.md#ga93504a76a265bedbe781c107beebc9dc)#define SPI\_TRANSFER\_LSB BIT(4)

92

98#define SPI\_WORD\_SIZE\_SHIFT (5U)

99#define SPI\_WORD\_SIZE\_MASK (0x3FU << SPI\_WORD\_SIZE\_SHIFT)

[ 102](group__spi__interface.md#ga7386c70bd669142bb7558526175765cc)#define SPI\_WORD\_SIZE\_GET(\_operation\_) \

103 (((\_operation\_) & SPI\_WORD\_SIZE\_MASK) >> SPI\_WORD\_SIZE\_SHIFT)

104

[ 105](group__spi__interface.md#gaaea60640bb9223bbaf94338d07d9d07c)#define SPI\_WORD\_SET(\_word\_size\_) \

106 ((\_word\_size\_) << SPI\_WORD\_SIZE\_SHIFT)

107

108

[ 114](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)#define SPI\_HOLD\_ON\_CS BIT(12)

[ 120](group__spi__interface.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)#define SPI\_LOCK\_ON BIT(13)

121

[ 129](group__spi__interface.md#ga44076fa14703997f7e3aefb2bfccd801)#define SPI\_CS\_ACTIVE\_HIGH BIT(14)

131

[ 141](group__spi__interface.md#ga7a183f157e8cb8b437857a0babbd923b)#define SPI\_LINES\_SINGLE (0U << 16)

[ 142](group__spi__interface.md#ga120ab60329d664d5d6e828f90251a98a)#define SPI\_LINES\_DUAL (1U << 16)

[ 143](group__spi__interface.md#ga30866b948e995224de854e10a428bda5)#define SPI\_LINES\_QUAD (2U << 16)

[ 144](group__spi__interface.md#ga512d76085e600886654b8541aab31cf7)#define SPI\_LINES\_OCTAL (3U << 16)

145

[ 146](group__spi__interface.md#gadc79f986c4b30fe5b263841cd8bb5676)#define SPI\_LINES\_MASK (0x3U << 16)

147

149

[ 157](structspi__cs__control.md)struct [spi\_cs\_control](structspi__cs__control.md) {

[ 165](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f);

[ 170](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629);

171};

172

[ 210](group__spi__interface.md#ga48aa19f45413d56b03596d10b72c732e)#define SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev) \

211 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_BUS(spi\_dev), cs\_gpios, \

212 DT\_REG\_ADDR(spi\_dev), {})

213

[ 223](group__spi__interface.md#ga88fefbfadb8184806123e1f935a4ff7c)#define SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET(inst) \

224 SPI\_CS\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

225

[ 264](group__spi__interface.md#ga4a2bce02956d8121da7b6099f6c097b9)#define SPI\_CS\_CONTROL\_INIT(node\_id, delay\_) \

265 { \

266 .gpio = SPI\_CS\_GPIOS\_DT\_SPEC\_GET(node\_id), \

267 .delay = (delay\_), \

268 }

269

[ 283](group__spi__interface.md#ga239bda66980ed0a349b7177100f7752c)#define SPI\_CS\_CONTROL\_INIT\_INST(inst, delay\_) \

284 SPI\_CS\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay\_)

285

290#if defined(CONFIG\_SPI\_EXTENDED\_MODES)

291typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

292#else

[ 293](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

294#endif

295

[ 299](structspi__config.md)struct [spi\_config](structspi__config.md) {

[ 301](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a);

[ 322](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) [operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829);

[ 324](structspi__config.md#a020ca853537483b9641c37be70ab6ca0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0);

[ 329](structspi__config.md#a537dbfe323fafedaa219de1be2097dde) struct [spi\_cs\_control](structspi__cs__control.md) [cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde);

330};

331

[ 345](group__spi__interface.md#ga822af066ee0829aee405c034bb967463)#define SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

346 { \

347 .frequency = DT\_PROP(node\_id, spi\_max\_frequency), \

348 .operation = (operation\_) | \

349 DT\_PROP(node\_id, duplex) | \

350 DT\_PROP(node\_id, frame\_format) | \

351 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpol), SPI\_MODE\_CPOL, (0)) | \

352 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpha), SPI\_MODE\_CPHA, (0)) | \

353 COND\_CODE\_1(DT\_PROP(node\_id, spi\_hold\_cs), SPI\_HOLD\_ON\_CS, (0)), \

354 .slave = DT\_REG\_ADDR(node\_id), \

355 .cs = SPI\_CS\_CONTROL\_INIT(node\_id, delay\_), \

356 }

357

[ 369](group__spi__interface.md#gadc1e7de7925603adfedbac35fdabc78a)#define SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_) \

370 SPI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)

371

[ 375](structspi__dt__spec.md)struct [spi\_dt\_spec](structspi__dt__spec.md) {

[ 377](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a) const struct [device](structdevice.md) \*[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

[ 379](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e) struct [spi\_config](structspi__config.md) [config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e);

380};

381

[ 400](group__spi__interface.md#gaec6a8fde1c3ec6349a601a2d5f7af785)#define SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_) \

401 { \

402 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

403 .config = SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

404 }

405

[ 417](group__spi__interface.md#ga91c595b7567af23b447c755d898608f3)#define SPI\_DT\_SPEC\_INST\_GET(inst, operation\_, delay\_) \

418 SPI\_DT\_SPEC\_GET(DT\_DRV\_INST(inst), operation\_, delay\_)

419

[ 423](structspi__buf.md)struct [spi\_buf](structspi__buf.md) {

[ 425](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba) void \*[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

[ 430](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) size\_t [len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

431};

432

[ 436](structspi__buf__set.md)struct [spi\_buf\_set](structspi__buf__set.md) {

[ 438](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67) const struct [spi\_buf](structspi__buf.md) \*[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67);

[ 440](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) size\_t [count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc);

441};

442

443#if defined(CONFIG\_SPI\_STATS)

444[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(spi)

445[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_bytes)

446[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(tx\_bytes)

447[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(transfer\_error)

448[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

449

450[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(spi)

451[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, rx\_bytes)

452[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, tx\_bytes)

453[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, transfer\_error)

454[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(spi);

455

459struct spi\_device\_state {

460 struct [device\_state](structdevice__state.md) devstate;

461 struct stats\_spi stats;

462};

463

467#define Z\_SPI\_GET\_STATS(dev\_) \

468 CONTAINER\_OF(dev\_->state, struct spi\_device\_state, devstate)->stats

469

475#define SPI\_STATS\_RX\_BYTES\_INCN(dev\_, n) \

476 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), rx\_bytes, n)

477

483#define SPI\_STATS\_TX\_BYTES\_INCN(dev\_, n) \

484 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), tx\_bytes, n)

485

493#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_) \

494 STATS\_INC(Z\_SPI\_GET\_STATS(dev\_), transfer\_error)

495

499#define Z\_SPI\_DEVICE\_STATE\_DEFINE(dev\_id) \

500 static struct spi\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

501 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

502

509#define Z\_SPI\_INIT\_FN(dev\_id, init\_fn) \

510 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

511 { \

512 struct spi\_device\_state \*state = \

513 CONTAINER\_OF(dev->state, struct spi\_device\_state, devstate); \

514 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 3, \

515 STATS\_NAME\_INIT\_PARMS(spi)); \

516 stats\_register(dev->name, &(state->stats.s\_hdr)); \

517 return init\_fn(dev); \

518 }

519

539#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

540 data\_ptr, cfg\_ptr, level, prio, \

541 api\_ptr, ...) \

542 Z\_SPI\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

543 Z\_SPI\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

544 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

545 DEVICE\_DT\_NAME(node\_id), \

546 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

547 pm\_device, \

548 data\_ptr, cfg\_ptr, level, prio, \

549 api\_ptr, \

550 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

551 \_\_VA\_ARGS\_\_)

552

553static inline void [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(const struct [device](structdevice.md) \*dev, int error,

554 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

555 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

556{

557 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx\_bytes;

558 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx\_bytes;

559

560 if (error) {

561 [SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)(dev);

562 }

563

564 if (tx\_bufs) {

565 tx\_bytes = tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

566 SPI\_STATS\_TX\_BYTES\_INCN(dev, tx\_bytes);

567 }

568

569 if (rx\_bufs) {

570 rx\_bytes = rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

571 SPI\_STATS\_RX\_BYTES\_INCN(dev, rx\_bytes);

572 }

573}

574

575#else /\*CONFIG\_SPI\_STATS\*/

576

[ 577](group__spi__interface.md#ga27af5f053c5fd4e9eef0900406fbf854)#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, \

578 data, config, level, prio, \

579 api, ...) \

580 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

581 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

582 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

583 level, prio, api, \

584 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

585 \_\_VA\_ARGS\_\_)

586

[ 587](group__spi__interface.md#ga83fa04d1e9f281cd566ee32cf807325e)#define SPI\_STATS\_RX\_BYTES\_INC(dev\_)

[ 588](group__spi__interface.md#gadd3b82af2396b91930ece09fa79fc4e2)#define SPI\_STATS\_TX\_BYTES\_INC(dev\_)

[ 589](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

590

[ 591](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

592

593#endif /\*CONFIG\_SPI\_STATS\*/

594

[ 600](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)typedef int (\*[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13))(const struct [device](structdevice.md) \*dev,

601 const struct [spi\_config](structspi__config.md) \*config,

602 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

603 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

604

[ 612](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)typedef void (\*[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d))(const struct [device](structdevice.md) \*dev, int result, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

613

[ 619](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)typedef int (\*[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7))(const struct [device](structdevice.md) \*dev,

620 const struct [spi\_config](structspi__config.md) \*config,

621 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

622 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

623 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb,

624 void \*userdata);

625

626#if defined(CONFIG\_SPI\_RTIO) || defined(DOXYGEN)

627

632typedef void (\*spi\_api\_iodev\_submit)(const struct [device](structdevice.md) \*dev,

633 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

634#endif /\* CONFIG\_SPI\_RTIO \*/

635

[ 641](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)typedef int (\*[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d))(const struct [device](structdevice.md) \*dev,

642 const struct [spi\_config](structspi__config.md) \*config);

643

644

[ 649](structspi__driver__api.md)\_\_subsystem struct [spi\_driver\_api](structspi__driver__api.md) {

[ 650](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb) [spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13) [transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb);

651#ifdef CONFIG\_SPI\_ASYNC

652 [spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7) transceive\_async;

653#endif /\* CONFIG\_SPI\_ASYNC \*/

654#ifdef CONFIG\_SPI\_RTIO

655 spi\_api\_iodev\_submit iodev\_submit;

656#endif /\* CONFIG\_SPI\_RTIO \*/

[ 657](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d) [spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d) [release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d);

658};

659

[ 667](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)static inline bool [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(const struct [spi\_config](structspi__config.md) \*config)

668{

669 return config->[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f).[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) != NULL;

670}

671

[ 679](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)static inline bool [spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

680{

681 return [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

682}

683

692\_\_deprecated

[ 693](group__spi__interface.md#ga7d5fcb15e3a1082ea63203b185c6a207)static inline bool [spi\_is\_ready](group__spi__interface.md#ga7d5fcb15e3a1082ea63203b185c6a207)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

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

[ 715](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)static inline bool [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

716{

717 /\* Validate bus is ready \*/

718 if (![device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a))) {

719 return false;

720 }

721 /\* Validate CS gpio port is ready, if it is used \*/

722 if ([spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(spec) &&

723 ![gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e).[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f))) {

724 return false;

725 }

726 return true;

727}

728

[ 747](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)\_\_syscall int [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(const struct [device](structdevice.md) \*dev,

748 const struct [spi\_config](structspi__config.md) \*config,

749 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

750 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

751

752static inline int z\_impl\_spi\_transceive(const struct [device](structdevice.md) \*dev,

753 const struct [spi\_config](structspi__config.md) \*config,

754 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

755 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

756{

757 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

758 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

759 int ret;

760

761 ret = api->transceive(dev, config, tx\_bufs, rx\_bufs);

762 [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, ret, tx\_bufs, rx\_bufs);

763

764 return ret;

765}

766

[ 782](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)static inline int [spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

783 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

784 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

785{

786 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs, rx\_bufs);

787}

788

[ 806](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)static inline int [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(const struct [device](structdevice.md) \*dev,

807 const struct [spi\_config](structspi__config.md) \*config,

808 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

809{

810 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, NULL, rx\_bufs);

811}

812

[ 825](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)static inline int [spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

826 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

827{

828 return [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), rx\_bufs);

829}

830

[ 847](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)static inline int [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(const struct [device](structdevice.md) \*dev,

848 const struct [spi\_config](structspi__config.md) \*config,

849 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

850{

851 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, tx\_bufs, NULL);

852}

853

[ 866](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)static inline int [spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

867 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

868{

869 return [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs);

870}

871

872#if defined(CONFIG\_SPI\_ASYNC) || defined(\_\_DOXYGEN\_\_)

873

[ 900](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)static inline int [spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)(const struct [device](structdevice.md) \*dev,

901 const struct [spi\_config](structspi__config.md) \*config,

902 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

903 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

904 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) callback,

905 void \*userdata)

906{

907 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

908 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

909

910 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, callback, userdata);

911}

912

913#if defined(CONFIG\_POLL) || defined(\_\_DOXYGEN\_\_)

914

916void z\_spi\_transfer\_signal\_cb(const struct [device](structdevice.md) \*dev, int result, void \*userdata);

918

[ 944](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)static inline int [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(const struct [device](structdevice.md) \*dev,

945 const struct [spi\_config](structspi__config.md) \*config,

946 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

947 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

948 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

949{

950 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

951 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

952 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb = (sig == NULL) ? NULL : z\_spi\_transfer\_signal\_cb;

953

954 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, cb, sig);

955}

956

[ 962](group__spi__interface.md#gacc26ab19d1211508691691308744350f)\_\_deprecated static inline int [spi\_transceive\_async](group__spi__interface.md#gacc26ab19d1211508691691308744350f)(const struct [device](structdevice.md) \*dev,

963 const struct [spi\_config](structspi__config.md) \*config,

964 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

965 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

966 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

967{

968 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, tx\_bufs, rx\_bufs, sig);

969}

970

[ 995](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)static inline int [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)(const struct [device](structdevice.md) \*dev,

996 const struct [spi\_config](structspi__config.md) \*config,

997 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

998 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

999{

1000 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, NULL, rx\_bufs, sig);

1001}

1002

[ 1008](group__spi__interface.md#ga5185c52f0c8e2e3419a16c6e24af55e1)\_\_deprecated static inline int [spi\_read\_async](group__spi__interface.md#ga5185c52f0c8e2e3419a16c6e24af55e1)(const struct [device](structdevice.md) \*dev,

1009 const struct [spi\_config](structspi__config.md) \*config,

1010 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1011 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1012{

1013 return [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)(dev, config, rx\_bufs, sig);

1014}

1015

[ 1039](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)static inline int [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)(const struct [device](structdevice.md) \*dev,

1040 const struct [spi\_config](structspi__config.md) \*config,

1041 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1042 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1043{

1044 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, tx\_bufs, NULL, sig);

1045}

1046

[ 1052](group__spi__interface.md#ga37d17fa9ae3909529762c43f9409d0f0)\_\_deprecated static inline int [spi\_write\_async](group__spi__interface.md#ga37d17fa9ae3909529762c43f9409d0f0)(const struct [device](structdevice.md) \*dev,

1053 const struct [spi\_config](structspi__config.md) \*config,

1054 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1055 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1056{

1057 return [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)(dev, config, tx\_bufs, sig);

1058}

1059

1060#endif /\* CONFIG\_POLL \*/

1061

1062#endif /\* CONFIG\_SPI\_ASYNC \*/

1063

1064

1065#if defined(CONFIG\_SPI\_RTIO) || defined(\_\_DOXYGEN\_\_)

1066

[ 1074](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)static inline void [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1075{

1076 const struct [spi\_dt\_spec](structspi__dt__spec.md) \*dt\_spec = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1077 const struct [device](structdevice.md) \*dev = dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

1078 const struct [spi\_driver\_api](structspi__driver__api.md) \*api = (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1079

1080 api->iodev\_submit(dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), iodev\_sqe);

1081}

1082

1083extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) [spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9);

1084

[ 1096](group__spi__interface.md#ga1e9f5fe389d53c280639f23ea134e18c)#define SPI\_DT\_IODEV\_DEFINE(name, node\_id, operation\_, delay\_) \

1097 const struct spi\_dt\_spec \_spi\_dt\_spec\_##name = \

1098 SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

1099 RTIO\_IODEV\_DEFINE(name, &spi\_iodev\_api, (void \*)&\_spi\_dt\_spec\_##name)

1100

[ 1109](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)static inline bool [spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)(const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev)

1110{

1111 struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec = spi\_iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1112

1113 return [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(spec);

1114}

1115

[ 1128](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)static inline int [spi\_rtio\_copy](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1129 struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

1130 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1131 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1132 struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe)

1133{

1134 int ret = 0;

1135 size\_t tx\_count = tx\_bufs ? tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) : 0;

1136 size\_t rx\_count = rx\_bufs ? rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) : 0;

1137

1138 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx = 0, tx\_len = 0;

1139 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx = 0, rx\_len = 0;

1140 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf, \*rx\_buf;

1141

1142 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = NULL;

1143

1144 if (tx < tx\_count) {

1145 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1146 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1147 } else {

1148 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1149 tx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1150 }

1151

1152 if (rx < rx\_count) {

1153 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1154 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1155 } else {

1156 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1157 rx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1158 }

1159

1160

1161 while ((tx < tx\_count || rx < rx\_count) && (tx\_len > 0 || rx\_len > 0)) {

1162 sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1163

1164 if (sqe == NULL) {

1165 ret = -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1166 [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2));

1167 goto out;

1168 }

1169

1170 ret++;

1171

1172 /\* If tx/rx len are same, we can do a simple transceive \*/

1173 if (tx\_len == rx\_len) {

1174 if ([tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) == NULL) {

1175 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1176 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73), rx\_len, NULL);

1177 } else if ([rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) == NULL) {

1178 [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1179 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a), tx\_len, NULL);

1180 } else {

1181 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1182 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a), [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73), rx\_len, NULL);

1183 }

1184 tx++;

1185 rx++;

1186 if (rx < rx\_count) {

1187 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1188 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1189 } else {

1190 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1191 rx\_len = 0;

1192 }

1193 if (tx < tx\_count) {

1194 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1195 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1196 } else {

1197 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1198 tx\_len = 0;

1199 }

1200 } else if (tx\_len == 0) {

1201 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1202 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1203 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))rx\_len,

1204 NULL);

1205 rx++;

1206 if (rx < rx\_count) {

1207 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1208 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1209 } else {

1210 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1211 rx\_len = 0;

1212 }

1213 } else if (rx\_len == 0) {

1214 [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1215 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1216 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))tx\_len,

1217 NULL);

1218 tx++;

1219 if (tx < tx\_count) {

1220 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1221 tx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1222 } else {

1223 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1224 tx\_len = 0;

1225 }

1226 } else if (tx\_len > rx\_len) {

1227 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1228 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1229 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1230 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))rx\_len,

1231 NULL);

1232 tx\_len -= rx\_len;

1233 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) += rx\_len;

1234 rx++;

1235 if (rx < rx\_count) {

1236 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1237 rx\_len = rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[rx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1238 } else {

1239 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) = NULL;

1240 rx\_len = tx\_len;

1241 }

1242 } else if (rx\_len > tx\_len) {

1243 [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92),

1244 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a),

1245 ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73),

1246 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))tx\_len,

1247 NULL);

1248 rx\_len -= tx\_len;

1249 [rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73) += tx\_len;

1250 tx++;

1251 if (tx < tx\_count) {

1252 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

1253 tx\_len = tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)[tx].[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

1254 } else {

1255 [tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a) = NULL;

1256 tx\_len = rx\_len;

1257 }

1258 } else {

1259 \_\_ASSERT\_NO\_MSG("Invalid spi\_rtio\_copy state");

1260 }

1261

1262 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea);

1263 }

1264

1265 if (sqe != NULL) {

1266 sqe->[flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0) = 0;

1267 \*last\_sqe = sqe;

1268 }

1269

1270out:

1271 return ret;

1272}

1273

1274#endif /\* CONFIG\_SPI\_RTIO \*/

1275

[ 1296](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)\_\_syscall int [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(const struct [device](structdevice.md) \*dev,

1297 const struct [spi\_config](structspi__config.md) \*config);

1298

1299static inline int z\_impl\_spi\_release(const struct [device](structdevice.md) \*dev,

1300 const struct [spi\_config](structspi__config.md) \*config)

1301{

1302 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1303 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1304

1305 return api->release(dev, config);

1306}

1307

[ 1319](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)static inline int [spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

1320{

1321 return [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1322}

1323

1324#ifdef \_\_cplusplus

1325}

1326#endif

1327

1331

1332#include <syscalls/spi.h>

1333

1334#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_ \*/

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

**Definition** gpio.h:831

[RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)

#define RTIO\_SQE\_TRANSACTION

The next request in the queue is part of a transaction.

**Definition** rtio.h:106

[RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)

#define RTIO\_PRIO\_NORM

Normal priority.

**Definition** rtio.h:68

[rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869)

static void rtio\_sqe\_prep\_transceive(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)

Prepare a transceive op submission.

**Definition** rtio.h:599

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:490

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:895

[rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b)

static void rtio\_sqe\_drop\_all(struct rtio \*r)

Drop all previously acquired sqe.

**Definition** rtio.h:913

[rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149)

static void rtio\_sqe\_prep\_write(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a write op submission.

**Definition** rtio.h:530

[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)

int(\* spi\_api\_io\_async)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t cb, void \*userdata)

**Definition** spi.h:619

[spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)

int spi\_release(const struct device \*dev, const struct spi\_config \*config)

Release the SPI device locked on and/or the CS by the current config.

[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)

void(\* spi\_callback\_t)(const struct device \*dev, int result, void \*data)

SPI callback for asynchronous transfer requests.

**Definition** spi.h:612

[spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)

static int spi\_write\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs)

Write data to a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:866

[spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)

static bool spi\_is\_ready\_dt(const struct spi\_dt\_spec \*spec)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:715

[spi\_write\_async](group__spi__interface.md#ga37d17fa9ae3909529762c43f9409d0f0)

static int spi\_write\_async(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, struct k\_poll\_signal \*sig)

Alias for spi\_write\_signal for backwards compatibility.

**Definition** spi.h:1052

[spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)

uint16\_t spi\_operation\_t

Opaque type to hold the SPI operation flags.

**Definition** spi.h:293

[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)

int(\* spi\_api\_io)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Callback API for I/O See spi\_transceive() for argument descriptions.

**Definition** spi.h:600

[spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)

static int spi\_transceive\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:944

[spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)

static int spi\_read(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:806

[spi\_read\_async](group__spi__interface.md#ga5185c52f0c8e2e3419a16c6e24af55e1)

static int spi\_read\_async(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Alias for spi\_read\_signal for backwards compatibility.

**Definition** spi.h:1008

[spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)

static int spi\_transceive\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write data from an SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:782

[spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)

static int spi\_transceive\_cb(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t callback, void \*userdata)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:900

[SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)

#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

**Definition** spi.h:589

[spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)

static int spi\_read\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*rx\_bufs)

Read data from a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:825

[spi\_is\_ready](group__spi__interface.md#ga7d5fcb15e3a1082ea63203b185c6a207)

static bool spi\_is\_ready(const struct spi\_dt\_spec \*spec)

Validate that SPI bus is ready.

**Definition** spi.h:693

[spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)

static int spi\_write(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:847

[spi\_rtio\_copy](group__spi__interface.md#ga812818433d437829fe6ab4fcff0ed38b)

static int spi\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct rtio\_sqe \*\*last\_sqe)

Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

**Definition** spi.h:1128

[spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)

static int spi\_release\_dt(const struct spi\_dt\_spec \*spec)

Release the SPI device specified in spi\_dt\_spec.

**Definition** spi.h:1319

[spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)

static void spi\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit a SPI device with a request.

**Definition** spi.h:1074

[spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)

static int spi\_read\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:995

[spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)

static bool spi\_cs\_is\_gpio\_dt(const struct spi\_dt\_spec \*spec)

Check if SPI CS in spi\_dt\_spec is controlled using a GPIO.

**Definition** spi.h:679

[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)

int(\* spi\_api\_release)(const struct device \*dev, const struct spi\_config \*config)

Callback API for unlocking SPI device.

**Definition** spi.h:641

[spi\_transceive\_async](group__spi__interface.md#gacc26ab19d1211508691691308744350f)

static int spi\_transceive\_async(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Alias for spi\_transceive\_signal for backwards compatibility.

**Definition** spi.h:962

[spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9)

const struct rtio\_iodev\_api spi\_iodev\_api

[spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)

int spi\_transceive(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write the specified amount of data from the SPI driver.

[spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)

#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

**Definition** spi.h:591

[spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)

static int spi\_write\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, struct k\_poll\_signal \*sig)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:1039

[spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)

static bool spi\_cs\_is\_gpio(const struct spi\_config \*config)

Check if SPI CS is controlled using a GPIO.

**Definition** spi.h:667

[spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)

static bool spi\_is\_ready\_iodev(const struct rtio\_iodev \*spi\_iodev)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:1109

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:51

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[rtio.h](rtio_8h.md)

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

**Definition** device.h:358

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:286

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:288

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:429

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:419

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:420

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:444

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:452

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:230

[rtio\_sqe::tx\_buf](structrtio__sqe.md#a186c22217961a5eddb75ad0bd84a538a)

uint8\_t \* tx\_buf

**Definition** rtio.h:275

[rtio\_sqe::rx\_buf](structrtio__sqe.md#a4d2090fc11b897724a883ad1087d9f73)

uint8\_t \* rx\_buf

**Definition** rtio.h:276

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:241

[rtio\_sqe::flags](structrtio__sqe.md#aad2ff8524df0e24b812e77e2393bf5b0)

uint16\_t flags

Op Flags.

**Definition** rtio.h:235

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:323

[spi\_buf\_set](structspi__buf__set.md)

SPI buffer array structure.

**Definition** spi.h:436

[spi\_buf\_set::buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)

const struct spi\_buf \* buffers

Pointer to an array of spi\_buf, or NULL.

**Definition** spi.h:438

[spi\_buf\_set::count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc)

size\_t count

Length of the array pointed by buffers.

**Definition** spi.h:440

[spi\_buf](structspi__buf.md)

SPI buffer structure.

**Definition** spi.h:423

[spi\_buf::len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba)

size\_t len

Length of the buffer buf.

**Definition** spi.h:430

[spi\_buf::buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba)

void \* buf

Valid pointer to a data buffer, or NULL otherwise.

**Definition** spi.h:425

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:299

[spi\_config::slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0)

uint16\_t slave

Slave number from 0 to host controller slave limit.

**Definition** spi.h:324

[spi\_config::cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde)

struct spi\_cs\_control cs

GPIO chip-select line (optional, must be initialized to zero if not used).

**Definition** spi.h:329

[spi\_config::operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829)

spi\_operation\_t operation

Operation flags.

**Definition** spi.h:322

[spi\_config::frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a)

uint32\_t frequency

Bus frequency in Hertz.

**Definition** spi.h:301

[spi\_cs\_control](structspi__cs__control.md)

SPI Chip Select control structure.

**Definition** spi.h:157

[spi\_cs\_control::delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629)

uint32\_t delay

Delay in microseconds to wait before starting the transmission and before releasing the CS line.

**Definition** spi.h:170

[spi\_cs\_control::gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f)

struct gpio\_dt\_spec gpio

GPIO devicetree specification of CS GPIO.

**Definition** spi.h:165

[spi\_driver\_api](structspi__driver__api.md)

SPI driver API This is the mandatory API any SPI driver needs to expose.

**Definition** spi.h:649

[spi\_driver\_api::transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb)

spi\_api\_io transceive

**Definition** spi.h:650

[spi\_driver\_api::release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d)

spi\_api\_release release

**Definition** spi.h:657

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:375

[spi\_dt\_spec::bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a)

const struct device \* bus

SPI bus.

**Definition** spi.h:377

[spi\_dt\_spec::config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e)

struct spi\_config config

Slave specific configuration.

**Definition** spi.h:379

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi.h](drivers_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
