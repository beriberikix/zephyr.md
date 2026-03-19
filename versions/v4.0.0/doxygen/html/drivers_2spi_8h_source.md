---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2spi_8h_source.html
original_path: doxygen/html/drivers_2spi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

214 DT\_REG\_ADDR\_RAW(spi\_dev), {})

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

[ 424](group__spi__interface.md#ga15b5fa509a3b7dc87bfd451af5a11917)#define SPI\_MOSI\_OVERRUN\_UNKNOWN 0x100

425

[ 438](group__spi__interface.md#gaa9621b033dfaf128602b1432927a67fe)#define SPI\_MOSI\_OVERRUN\_DT(node\_id) \

439 DT\_PROP\_OR(node\_id, overrun\_character, SPI\_MOSI\_OVERRUN\_UNKNOWN)

440

[ 452](group__spi__interface.md#ga24c7416a98421e353a8892151f34122c)#define SPI\_MOSI\_OVERRUN\_DT\_INST(inst) \

453 DT\_INST\_PROP\_OR(inst, overrun\_character, SPI\_MOSI\_OVERRUN\_UNKNOWN)

454

[ 458](structspi__buf.md)struct [spi\_buf](structspi__buf.md) {

[ 460](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba) void \*[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

[ 465](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) size\_t [len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

466};

467

[ 471](structspi__buf__set.md)struct [spi\_buf\_set](structspi__buf__set.md) {

[ 473](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67) const struct [spi\_buf](structspi__buf.md) \*[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67);

[ 475](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) size\_t [count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc);

476};

477

478#if defined(CONFIG\_SPI\_STATS)

479[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(spi)

480[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_bytes)

481[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(tx\_bytes)

482[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(transfer\_error)

483[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

484

485[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(spi)

486[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, rx\_bytes)

487[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, tx\_bytes)

488[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, transfer\_error)

489[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(spi);

490

494struct spi\_device\_state {

495 struct [device\_state](structdevice__state.md) devstate;

496 struct stats\_spi stats;

497};

498

502#define Z\_SPI\_GET\_STATS(dev\_) \

503 CONTAINER\_OF(dev\_->state, struct spi\_device\_state, devstate)->stats

504

510#define SPI\_STATS\_RX\_BYTES\_INCN(dev\_, n) \

511 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), rx\_bytes, n)

512

518#define SPI\_STATS\_TX\_BYTES\_INCN(dev\_, n) \

519 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), tx\_bytes, n)

520

528#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_) \

529 STATS\_INC(Z\_SPI\_GET\_STATS(dev\_), transfer\_error)

530

534#define Z\_SPI\_DEVICE\_STATE\_DEFINE(dev\_id) \

535 static struct spi\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

536 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

537

544#define Z\_SPI\_INIT\_FN(dev\_id, init\_fn) \

545 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

546 { \

547 struct spi\_device\_state \*state = \

548 CONTAINER\_OF(dev->state, struct spi\_device\_state, devstate); \

549 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 3, \

550 STATS\_NAME\_INIT\_PARMS(spi)); \

551 stats\_register(dev->name, &(state->stats.s\_hdr)); \

552 return init\_fn(dev); \

553 }

554

574#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

575 data\_ptr, cfg\_ptr, level, prio, \

576 api\_ptr, ...) \

577 Z\_SPI\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

578 Z\_SPI\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

579 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

580 DEVICE\_DT\_NAME(node\_id), \

581 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

582 pm\_device, \

583 data\_ptr, cfg\_ptr, level, prio, \

584 api\_ptr, \

585 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

586 \_\_VA\_ARGS\_\_)

587

588static inline void [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(const struct [device](structdevice.md) \*dev, int error,

589 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

590 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

591{

592 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx\_bytes;

593 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx\_bytes;

594

595 if (error) {

596 [SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)(dev);

597 }

598

599 if (tx\_bufs) {

600 tx\_bytes = tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

601 SPI\_STATS\_TX\_BYTES\_INCN(dev, tx\_bytes);

602 }

603

604 if (rx\_bufs) {

605 rx\_bytes = rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

606 SPI\_STATS\_RX\_BYTES\_INCN(dev, rx\_bytes);

607 }

608}

609

610#else /\*CONFIG\_SPI\_STATS\*/

611

[ 612](group__spi__interface.md#ga27af5f053c5fd4e9eef0900406fbf854)#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, \

613 data, config, level, prio, \

614 api, ...) \

615 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

616 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

617 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

618 level, prio, api, \

619 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

620 \_\_VA\_ARGS\_\_)

621

[ 622](group__spi__interface.md#ga83fa04d1e9f281cd566ee32cf807325e)#define SPI\_STATS\_RX\_BYTES\_INC(dev\_)

[ 623](group__spi__interface.md#gadd3b82af2396b91930ece09fa79fc4e2)#define SPI\_STATS\_TX\_BYTES\_INC(dev\_)

[ 624](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

625

[ 626](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

627

628#endif /\*CONFIG\_SPI\_STATS\*/

629

[ 635](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)typedef int (\*[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13))(const struct [device](structdevice.md) \*dev,

636 const struct [spi\_config](structspi__config.md) \*config,

637 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

638 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

639

[ 647](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)typedef void (\*[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d))(const struct [device](structdevice.md) \*dev, int result, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

648

[ 654](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)typedef int (\*[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7))(const struct [device](structdevice.md) \*dev,

655 const struct [spi\_config](structspi__config.md) \*config,

656 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

657 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

658 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb,

659 void \*userdata);

660

661#if defined(CONFIG\_SPI\_RTIO) || defined(DOXYGEN)

662

667typedef void (\*spi\_api\_iodev\_submit)(const struct [device](structdevice.md) \*dev,

668 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

669#endif /\* CONFIG\_SPI\_RTIO \*/

670

[ 676](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)typedef int (\*[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d))(const struct [device](structdevice.md) \*dev,

677 const struct [spi\_config](structspi__config.md) \*config);

678

679

[ 684](structspi__driver__api.md)\_\_subsystem struct [spi\_driver\_api](structspi__driver__api.md) {

[ 685](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb) [spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13) [transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb);

686#ifdef CONFIG\_SPI\_ASYNC

687 [spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7) transceive\_async;

688#endif /\* CONFIG\_SPI\_ASYNC \*/

689#ifdef CONFIG\_SPI\_RTIO

690 spi\_api\_iodev\_submit iodev\_submit;

691#endif /\* CONFIG\_SPI\_RTIO \*/

[ 692](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d) [spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d) [release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d);

693};

694

[ 702](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)static inline bool [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(const struct [spi\_config](structspi__config.md) \*config)

703{

704 return config->[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f).[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) != NULL;

705}

706

[ 714](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)static inline bool [spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

715{

716 return [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

717}

718

[ 727](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)static inline bool [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

728{

729 /\* Validate bus is ready \*/

730 if (![device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a))) {

731 return false;

732 }

733 /\* Validate CS gpio port is ready, if it is used \*/

734 if ([spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(spec) &&

735 ![gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e).[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f))) {

736 return false;

737 }

738 return true;

739}

740

[ 759](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)\_\_syscall int [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(const struct [device](structdevice.md) \*dev,

760 const struct [spi\_config](structspi__config.md) \*config,

761 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

762 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

763

764static inline int z\_impl\_spi\_transceive(const struct [device](structdevice.md) \*dev,

765 const struct [spi\_config](structspi__config.md) \*config,

766 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

767 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

768{

769 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

770 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

771 int ret;

772

773 ret = api->transceive(dev, config, tx\_bufs, rx\_bufs);

774 [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, ret, tx\_bufs, rx\_bufs);

775

776 return ret;

777}

778

[ 794](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)static inline int [spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

795 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

796 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

797{

798 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs, rx\_bufs);

799}

800

[ 818](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)static inline int [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(const struct [device](structdevice.md) \*dev,

819 const struct [spi\_config](structspi__config.md) \*config,

820 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

821{

822 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, NULL, rx\_bufs);

823}

824

[ 837](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)static inline int [spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

838 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

839{

840 return [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), rx\_bufs);

841}

842

[ 859](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)static inline int [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(const struct [device](structdevice.md) \*dev,

860 const struct [spi\_config](structspi__config.md) \*config,

861 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

862{

863 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, tx\_bufs, NULL);

864}

865

[ 878](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)static inline int [spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

879 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

880{

881 return [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs);

882}

883

884#if defined(CONFIG\_SPI\_ASYNC) || defined(\_\_DOXYGEN\_\_)

885

[ 912](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)static inline int [spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)(const struct [device](structdevice.md) \*dev,

913 const struct [spi\_config](structspi__config.md) \*config,

914 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

915 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

916 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) callback,

917 void \*userdata)

918{

919 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

920 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

921

922 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, callback, userdata);

923}

924

925#if defined(CONFIG\_POLL) || defined(\_\_DOXYGEN\_\_)

926

928void z\_spi\_transfer\_signal\_cb(const struct [device](structdevice.md) \*dev, int result, void \*userdata);

930

[ 956](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)static inline int [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(const struct [device](structdevice.md) \*dev,

957 const struct [spi\_config](structspi__config.md) \*config,

958 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

959 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

960 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

961{

962 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

963 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

964 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb = (sig == NULL) ? NULL : z\_spi\_transfer\_signal\_cb;

965

966 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, cb, sig);

967}

968

[ 993](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)static inline int [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)(const struct [device](structdevice.md) \*dev,

994 const struct [spi\_config](structspi__config.md) \*config,

995 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

996 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

997{

998 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, NULL, rx\_bufs, sig);

999}

1000

[ 1024](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)static inline int [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)(const struct [device](structdevice.md) \*dev,

1025 const struct [spi\_config](structspi__config.md) \*config,

1026 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1027 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1028{

1029 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, tx\_bufs, NULL, sig);

1030}

1031

1032#endif /\* CONFIG\_POLL \*/

1033

1034#endif /\* CONFIG\_SPI\_ASYNC \*/

1035

1036

1037#if defined(CONFIG\_SPI\_RTIO) || defined(\_\_DOXYGEN\_\_)

1038

[ 1046](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)static inline void [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1047{

1048 const struct [spi\_dt\_spec](structspi__dt__spec.md) \*dt\_spec = iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1049 const struct [device](structdevice.md) \*dev = dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

1050 const struct [spi\_driver\_api](structspi__driver__api.md) \*api = (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1051

1052 api->iodev\_submit(dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), iodev\_sqe);

1053}

1054

1055extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) [spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9);

1056

[ 1068](group__spi__interface.md#ga1e9f5fe389d53c280639f23ea134e18c)#define SPI\_DT\_IODEV\_DEFINE(name, node\_id, operation\_, delay\_) \

1069 const struct spi\_dt\_spec \_spi\_dt\_spec\_##name = \

1070 SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

1071 RTIO\_IODEV\_DEFINE(name, &spi\_iodev\_api, (void \*)&\_spi\_dt\_spec\_##name)

1072

[ 1081](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)static inline bool [spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)(const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev)

1082{

1083 struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec = spi\_iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1084

1085 return [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(spec);

1086}

1087

1088#endif /\* CONFIG\_SPI\_RTIO \*/

1089

[ 1110](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)\_\_syscall int [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(const struct [device](structdevice.md) \*dev,

1111 const struct [spi\_config](structspi__config.md) \*[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1112

1113static inline int z\_impl\_spi\_release(const struct [device](structdevice.md) \*dev,

1114 const struct [spi\_config](structspi__config.md) \*[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e))

1115{

1116 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1117 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1118

1119 return api->release(dev, config);

1120}

1121

[ 1133](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)static inline int [spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

1134{

1135 return [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1136}

1137

1138#ifdef \_\_cplusplus

1139}

1140#endif

1141

1145

1146#include <zephyr/syscalls/spi.h>

1147

1148#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

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

[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)

int(\* spi\_api\_io\_async)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t cb, void \*userdata)

**Definition** spi.h:654

[spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)

int spi\_release(const struct device \*dev, const struct spi\_config \*config)

Release the SPI device locked on and/or the CS by the current config.

[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)

void(\* spi\_callback\_t)(const struct device \*dev, int result, void \*data)

SPI callback for asynchronous transfer requests.

**Definition** spi.h:647

[spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)

static int spi\_write\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs)

Write data to a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:878

[spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)

static bool spi\_is\_ready\_dt(const struct spi\_dt\_spec \*spec)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:727

[spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)

uint16\_t spi\_operation\_t

Opaque type to hold the SPI operation flags.

**Definition** spi.h:295

[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)

int(\* spi\_api\_io)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Callback API for I/O See spi\_transceive() for argument descriptions.

**Definition** spi.h:635

[spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)

static int spi\_transceive\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:956

[spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)

static int spi\_read(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:818

[spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)

static int spi\_transceive\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write data from an SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:794

[spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)

static int spi\_transceive\_cb(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t callback, void \*userdata)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:912

[SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)

#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

**Definition** spi.h:624

[spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)

static int spi\_read\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*rx\_bufs)

Read data from a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:837

[spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)

static int spi\_write(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:859

[spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)

static int spi\_release\_dt(const struct spi\_dt\_spec \*spec)

Release the SPI device specified in spi\_dt\_spec.

**Definition** spi.h:1133

[spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)

static void spi\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit a SPI device with a request.

**Definition** spi.h:1046

[spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)

static int spi\_read\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:993

[spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)

static bool spi\_cs\_is\_gpio\_dt(const struct spi\_dt\_spec \*spec)

Check if SPI CS in spi\_dt\_spec is controlled using a GPIO.

**Definition** spi.h:714

[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)

int(\* spi\_api\_release)(const struct device \*dev, const struct spi\_config \*config)

Callback API for unlocking SPI device.

**Definition** spi.h:676

[spi\_iodev\_api](group__spi__interface.md#gacd22d734b1b2729e09862065d44b8ce9)

const struct rtio\_iodev\_api spi\_iodev\_api

[spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)

int spi\_transceive(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write the specified amount of data from the SPI driver.

[spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)

#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

**Definition** spi.h:626

[spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)

static int spi\_write\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, struct k\_poll\_signal \*sig)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:1024

[spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)

static bool spi\_cs\_is\_gpio(const struct spi\_config \*config)

Check if SPI CS is controlled using a GPIO.

**Definition** spi.h:702

[spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)

static bool spi\_is\_ready\_iodev(const struct rtio\_iodev \*spi\_iodev)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:1081

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

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:380

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:290

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5768

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:439

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:429

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:430

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:454

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:459

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[spi\_buf\_set](structspi__buf__set.md)

SPI buffer array structure.

**Definition** spi.h:471

[spi\_buf\_set::buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)

const struct spi\_buf \* buffers

Pointer to an array of spi\_buf, or NULL.

**Definition** spi.h:473

[spi\_buf\_set::count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc)

size\_t count

Length of the array (number of buffers) pointed by buffers.

**Definition** spi.h:475

[spi\_buf](structspi__buf.md)

SPI buffer structure.

**Definition** spi.h:458

[spi\_buf::len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba)

size\_t len

Length of the buffer buf in bytes.

**Definition** spi.h:465

[spi\_buf::buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba)

void \* buf

Valid pointer to a data buffer, or NULL otherwise.

**Definition** spi.h:460

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

**Definition** spi.h:684

[spi\_driver\_api::transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb)

spi\_api\_io transceive

**Definition** spi.h:685

[spi\_driver\_api::release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d)

spi\_api\_release release

**Definition** spi.h:692

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
