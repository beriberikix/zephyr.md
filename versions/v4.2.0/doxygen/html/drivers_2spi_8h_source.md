---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2spi_8h_source.html
original_path: doxygen/html/drivers_2spi_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

42

[ 50](group__spi__interface.md#ga5b9d40fa0f455b1e63f8040b3316b0da)#define SPI\_OP\_MODE\_MASTER 0U

51

[ 60](group__spi__interface.md#ga1c3310d3711cb99cdb78fa9d1c970779)#define SPI\_OP\_MODE\_SLAVE BIT(0)

61

63#define SPI\_OP\_MODE\_MASK 0x1U

65

[ 69](group__spi__interface.md#ga6dd4395e027407a7b3b92cff2abcc8b3)#define SPI\_OP\_MODE\_GET(\_operation\_) ((\_operation\_) & SPI\_OP\_MODE\_MASK)

71

72

77

[ 87](group__spi__interface.md#ga5a2be1003873beaa0ade10e7218d67d5)#define SPI\_MODE\_CPOL BIT(1)

88

[ 98](group__spi__interface.md#ga35e98b37e3ec4889a90100abe884590f)#define SPI\_MODE\_CPHA BIT(2)

99

[ 109](group__spi__interface.md#ga8619b297de563eca6852af34c79daa62)#define SPI\_MODE\_LOOP BIT(3)

110

112#define SPI\_MODE\_MASK (0xEU)

114

[ 118](group__spi__interface.md#gaa3582b96ff42dba0b0ad815c727d5e42)#define SPI\_MODE\_GET(\_mode\_) \

119 ((\_mode\_) & SPI\_MODE\_MASK)

120

122

123

135

[ 137](group__spi__interface.md#ga7761f42c6241cf396fc02d0de8617e46)#define SPI\_TRANSFER\_MSB (0U)

[ 139](group__spi__interface.md#ga93504a76a265bedbe781c107beebc9dc)#define SPI\_TRANSFER\_LSB BIT(4)

140

142#define SPI\_WORD\_SIZE\_SHIFT (5U)

143#define SPI\_WORD\_SIZE\_MASK (0x3FU << SPI\_WORD\_SIZE\_SHIFT)

145

[ 152](group__spi__interface.md#gacd7edd9ce02bd8351f8eebe5b5c07c7a)#define SPI\_WORD\_SIZE\_GET(operation) \

153 (((operation) & SPI\_WORD\_SIZE\_MASK) >> SPI\_WORD\_SIZE\_SHIFT)

154

[ 161](group__spi__interface.md#gac1115bf80134efd38d88161e3f5e3e1a)#define SPI\_WORD\_SET(word\_size) \

162 ((word\_size) << SPI\_WORD\_SIZE\_SHIFT)

163

165

166

171

[ 179](group__spi__interface.md#gae917312adef283b4bf67cdb53566e4bb)#define SPI\_HOLD\_ON\_CS BIT(12)

180

[ 194](group__spi__interface.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)#define SPI\_LOCK\_ON BIT(13)

195

[ 207](group__spi__interface.md#ga44076fa14703997f7e3aefb2bfccd801)#define SPI\_CS\_ACTIVE\_HIGH BIT(14)

208

210

211

[ 221](group__spi__interface.md#ga7a183f157e8cb8b437857a0babbd923b)#define SPI\_LINES\_SINGLE (0U << 16)

[ 222](group__spi__interface.md#ga120ab60329d664d5d6e828f90251a98a)#define SPI\_LINES\_DUAL (1U << 16)

[ 223](group__spi__interface.md#ga30866b948e995224de854e10a428bda5)#define SPI\_LINES\_QUAD (2U << 16)

[ 224](group__spi__interface.md#ga512d76085e600886654b8541aab31cf7)#define SPI\_LINES\_OCTAL (3U << 16)

225

[ 226](group__spi__interface.md#gadc79f986c4b30fe5b263841cd8bb5676)#define SPI\_LINES\_MASK (0x3U << 16)

227

229

234

[ 242](structspi__cs__control.md)struct [spi\_cs\_control](structspi__cs__control.md) {

[ 250](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f);

[ 255](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629);

256};

257

[ 295](group__spi__interface.md#ga48aa19f45413d56b03596d10b72c732e)#define SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev) \

296 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_BUS(spi\_dev), cs\_gpios, \

297 DT\_REG\_ADDR\_RAW(spi\_dev), {})

298

[ 308](group__spi__interface.md#ga88fefbfadb8184806123e1f935a4ff7c)#define SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET(inst) \

309 SPI\_CS\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

310

[ 349](group__spi__interface.md#ga4a2bce02956d8121da7b6099f6c097b9)#define SPI\_CS\_CONTROL\_INIT(node\_id, delay\_) \

350 { \

351 .gpio = SPI\_CS\_GPIOS\_DT\_SPEC\_GET(node\_id), \

352 .delay = (delay\_), \

353 }

354

[ 368](group__spi__interface.md#ga239bda66980ed0a349b7177100f7752c)#define SPI\_CS\_CONTROL\_INIT\_INST(inst, delay\_) \

369 SPI\_CS\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay\_)

370

372

377#if defined(CONFIG\_SPI\_EXTENDED\_MODES)

378typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

379#else

[ 380](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a);

381#endif

382

[ 390](structspi__config.md)struct [spi\_config](structspi__config.md) {

[ 392](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a);

[ 413](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829) [spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a) [operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829);

[ 415](structspi__config.md#a020ca853537483b9641c37be70ab6ca0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0);

[ 420](structspi__config.md#a537dbfe323fafedaa219de1be2097dde) struct [spi\_cs\_control](structspi__cs__control.md) [cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde);

421};

422

[ 436](group__spi__interface.md#ga822af066ee0829aee405c034bb967463)#define SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

437 { \

438 .frequency = DT\_PROP(node\_id, spi\_max\_frequency), \

439 .operation = (operation\_) | \

440 DT\_PROP(node\_id, duplex) | \

441 DT\_PROP(node\_id, frame\_format) | \

442 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpol), SPI\_MODE\_CPOL, (0)) | \

443 COND\_CODE\_1(DT\_PROP(node\_id, spi\_cpha), SPI\_MODE\_CPHA, (0)) | \

444 COND\_CODE\_1(DT\_PROP(node\_id, spi\_hold\_cs), SPI\_HOLD\_ON\_CS, (0)), \

445 .slave = DT\_REG\_ADDR(node\_id), \

446 .cs = SPI\_CS\_CONTROL\_INIT(node\_id, delay\_), \

447 }

448

[ 460](group__spi__interface.md#gadc1e7de7925603adfedbac35fdabc78a)#define SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_) \

461 SPI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)

462

[ 466](structspi__dt__spec.md)struct [spi\_dt\_spec](structspi__dt__spec.md) {

[ 468](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a) const struct [device](structdevice.md) \*[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

[ 470](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e) struct [spi\_config](structspi__config.md) [config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e);

471};

472

[ 490](group__spi__interface.md#gaec6a8fde1c3ec6349a601a2d5f7af785)#define SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_) \

491 { \

492 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

493 .config = SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

494 }

495

[ 507](group__spi__interface.md#ga91c595b7567af23b447c755d898608f3)#define SPI\_DT\_SPEC\_INST\_GET(inst, operation\_, delay\_) \

508 SPI\_DT\_SPEC\_GET(DT\_DRV\_INST(inst), operation\_, delay\_)

509

[ 513](group__spi__interface.md#ga15b5fa509a3b7dc87bfd451af5a11917)#define SPI\_MOSI\_OVERRUN\_UNKNOWN 0x100

514

[ 527](group__spi__interface.md#gaa9621b033dfaf128602b1432927a67fe)#define SPI\_MOSI\_OVERRUN\_DT(node\_id) \

528 DT\_PROP\_OR(node\_id, overrun\_character, SPI\_MOSI\_OVERRUN\_UNKNOWN)

529

[ 541](group__spi__interface.md#ga24c7416a98421e353a8892151f34122c)#define SPI\_MOSI\_OVERRUN\_DT\_INST(inst) \

542 DT\_INST\_PROP\_OR(inst, overrun\_character, SPI\_MOSI\_OVERRUN\_UNKNOWN)

543

[ 552](structspi__buf.md)struct [spi\_buf](structspi__buf.md) {

[ 554](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba) void \*[buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba);

[ 556](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) size\_t [len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba);

557};

558

[ 570](structspi__buf__set.md)struct [spi\_buf\_set](structspi__buf__set.md) {

[ 572](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67) const struct [spi\_buf](structspi__buf.md) \*[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67);

[ 574](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) size\_t [count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc);

575};

576

581#if defined(CONFIG\_SPI\_STATS)

582[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(spi)

583[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_bytes)

584[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(tx\_bytes)

585[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(transfer\_error)

586[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

587

588[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(spi)

589[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, rx\_bytes)

590[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, tx\_bytes)

591[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(spi, transfer\_error)

592[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(spi);

593

597struct spi\_device\_state {

598 struct [device\_state](structdevice__state.md) devstate;

599 struct stats\_spi stats;

600};

601

605#define Z\_SPI\_GET\_STATS(dev\_) \

606 CONTAINER\_OF(dev\_->state, struct spi\_device\_state, devstate)->stats

607

613#define SPI\_STATS\_RX\_BYTES\_INCN(dev\_, n) \

614 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), rx\_bytes, n)

615

621#define SPI\_STATS\_TX\_BYTES\_INCN(dev\_, n) \

622 STATS\_INCN(Z\_SPI\_GET\_STATS(dev\_), tx\_bytes, n)

623

631#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_) \

632 STATS\_INC(Z\_SPI\_GET\_STATS(dev\_), transfer\_error)

633

638#define Z\_SPI\_DEVICE\_STATE\_DEFINE(dev\_id) \

639 static struct spi\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

640 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")));

641

648#define Z\_SPI\_INIT\_FN(dev\_id, init\_fn) \

649 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

650 { \

651 struct spi\_device\_state \*state = \

652 CONTAINER\_OF(dev->state, struct spi\_device\_state, devstate); \

653 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 3, \

654 STATS\_NAME\_INIT\_PARMS(spi)); \

655 stats\_register(dev->name, &(state->stats.s\_hdr)); \

656 return init\_fn(dev); \

657 }

659

660#define SPI\_DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, deinit\_fn, \

661 pm\_device, data\_ptr, cfg\_ptr, \

662 level, prio, api\_ptr, ...) \

663 Z\_SPI\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

664 Z\_SPI\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

665 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

666 DEVICE\_DT\_NAME(node\_id), \

667 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

668 deinit\_fn, Z\_DEVICE\_DT\_FLAGS(node\_id), \

669 pm\_device, data\_ptr, cfg\_ptr, level, prio, \

670 api\_ptr, \

671 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

672 \_\_VA\_ARGS\_\_)

673

674static inline void [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(const struct [device](structdevice.md) \*dev, int error,

675 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

676 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

677{

678 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tx\_bytes;

679 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rx\_bytes;

680

681 if (error) {

682 [SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)(dev);

683 }

684

685 if (tx\_bufs) {

686 tx\_bytes = tx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? tx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

687 SPI\_STATS\_TX\_BYTES\_INCN(dev, tx\_bytes);

688 }

689

690 if (rx\_bufs) {

691 rx\_bytes = rx\_bufs->[count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc) ? rx\_bufs->[buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)->[len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba) : 0;

692 SPI\_STATS\_RX\_BYTES\_INCN(dev, rx\_bytes);

693 }

694}

696

697#else /\*CONFIG\_SPI\_STATS\*/

698

703

[ 724](group__spi__interface.md#gaf98b0cb38cb316b9fe05146bba34126d)#define SPI\_DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, deinit\_fn, pm, data, \

725 config, level, prio, api, ...) \

726 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

727 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

728 DEVICE\_DT\_NAME(node\_id), init\_fn, deinit\_fn, \

729 Z\_DEVICE\_DT\_FLAGS(node\_id), pm, data, config, \

730 level, prio, api, \

731 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

732 \_\_VA\_ARGS\_\_)

733

735

[ 736](group__spi__interface.md#ga83fa04d1e9f281cd566ee32cf807325e)#define SPI\_STATS\_RX\_BYTES\_INC(dev\_)

[ 737](group__spi__interface.md#gadd3b82af2396b91930ece09fa79fc4e2)#define SPI\_STATS\_TX\_BYTES\_INC(dev\_)

[ 738](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

739

[ 740](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

741

742#endif /\*CONFIG\_SPI\_STATS\*/

743

[ 763](group__spi__interface.md#ga27af5f053c5fd4e9eef0900406fbf854)#define SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, \

764 api, ...) \

765 SPI\_DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, NULL, pm, data, config, \

766 level, prio, api, \_\_VA\_ARGS\_\_)

767

[ 776](group__spi__interface.md#ga50cbb6845d230033f192f1e716fd9f2b)#define SPI\_DEVICE\_DT\_INST\_DEINIT\_DEFINE(inst, ...) \

777 SPI\_DEVICE\_DT\_DEINIT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

778

[ 787](group__spi__interface.md#ga84811e0fdd574477c8569d559f773dae)#define SPI\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

788 SPI\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

789

[ 795](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)typedef int (\*[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13))(const struct [device](structdevice.md) \*dev,

796 const struct [spi\_config](structspi__config.md) \*config,

797 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

798 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

799

[ 807](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)typedef void (\*[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d))(const struct [device](structdevice.md) \*dev, int result, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

808

[ 814](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)typedef int (\*[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7))(const struct [device](structdevice.md) \*dev,

815 const struct [spi\_config](structspi__config.md) \*config,

816 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

817 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

818 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb,

819 void \*userdata);

820

821#if defined(CONFIG\_SPI\_RTIO) || defined(DOXYGEN)

822

827typedef void (\*spi\_api\_iodev\_submit)(const struct [device](structdevice.md) \*dev,

828 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

829#endif /\* CONFIG\_SPI\_RTIO \*/

830

[ 836](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)typedef int (\*[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d))(const struct [device](structdevice.md) \*dev,

837 const struct [spi\_config](structspi__config.md) \*config);

838

839

[ 844](structspi__driver__api.md)\_\_subsystem struct [spi\_driver\_api](structspi__driver__api.md) {

[ 845](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb) [spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13) [transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb);

846#ifdef CONFIG\_SPI\_ASYNC

847 [spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7) transceive\_async;

848#endif /\* CONFIG\_SPI\_ASYNC \*/

849#ifdef CONFIG\_SPI\_RTIO

850 spi\_api\_iodev\_submit iodev\_submit;

851#endif /\* CONFIG\_SPI\_RTIO \*/

[ 852](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d) [spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d) [release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d);

853};

854

[ 862](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)static inline bool [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(const struct [spi\_config](structspi__config.md) \*config)

863{

864 return config->[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f).[port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

865}

866

[ 874](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)static inline bool [spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

875{

876 return [spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

877}

878

[ 887](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)static inline bool [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

888{

889 /\* Validate bus is ready \*/

890 if (![device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a))) {

891 return false;

892 }

893 /\* Validate CS gpio port is ready, if it is used \*/

894 if ([spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)(spec) &&

895 ![gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327)(&spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e).[cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde).[gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f))) {

896 return false;

897 }

898 return true;

899}

900

908

[ 939](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)\_\_syscall int [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(const struct [device](structdevice.md) \*dev,

940 const struct [spi\_config](structspi__config.md) \*config,

941 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

942 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

943

944static inline int z\_impl\_spi\_transceive(const struct [device](structdevice.md) \*dev,

945 const struct [spi\_config](structspi__config.md) \*config,

946 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

947 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

948{

949 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

950 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

951 int ret;

952

953 ret = api->transceive(dev, config, tx\_bufs, rx\_bufs);

954 [spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)(dev, ret, tx\_bufs, rx\_bufs);

955

956 return ret;

957}

958

[ 974](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)static inline int [spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

975 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

976 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

977{

978 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs, rx\_bufs);

979}

980

[ 1001](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)static inline int [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(const struct [device](structdevice.md) \*dev,

1002 const struct [spi\_config](structspi__config.md) \*config,

1003 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

1004{

1005 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), rx\_bufs);

1006}

1007

[ 1020](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)static inline int [spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

1021 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs)

1022{

1023 return [spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), rx\_bufs);

1024}

1025

[ 1045](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)static inline int [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(const struct [device](structdevice.md) \*dev,

1046 const struct [spi\_config](structspi__config.md) \*config,

1047 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

1048{

1049 return [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)(dev, config, tx\_bufs, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

1050}

1051

[ 1064](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)static inline int [spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec,

1065 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs)

1066{

1067 return [spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e), tx\_bufs);

1068}

1069

1070

1071#if defined(CONFIG\_SPI\_ASYNC) || defined(\_\_DOXYGEN\_\_)

1083

[ 1116](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)static inline int [spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)(const struct [device](structdevice.md) \*dev,

1117 const struct [spi\_config](structspi__config.md) \*config,

1118 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1119 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1120 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) callback,

1121 void \*userdata)

1122{

1123 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1124 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1125

1126 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, callback, userdata);

1127}

1128

1129#if defined(CONFIG\_POLL) || defined(\_\_DOXYGEN\_\_)

1130

1132void z\_spi\_transfer\_signal\_cb(const struct [device](structdevice.md) \*dev, int result, void \*userdata);

1134

[ 1166](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)static inline int [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(const struct [device](structdevice.md) \*dev,

1167 const struct [spi\_config](structspi__config.md) \*config,

1168 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1169 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1170 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1171{

1172 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1173 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1174 [spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d) cb = (sig == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : z\_spi\_transfer\_signal\_cb;

1175

1176 return api->transceive\_async(dev, config, tx\_bufs, rx\_bufs, cb, sig);

1177}

1178

[ 1206](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)static inline int [spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)(const struct [device](structdevice.md) \*dev,

1207 const struct [spi\_config](structspi__config.md) \*config,

1208 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

1209 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1210{

1211 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), rx\_bufs, sig);

1212}

1213

[ 1240](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)static inline int [spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)(const struct [device](structdevice.md) \*dev,

1241 const struct [spi\_config](structspi__config.md) \*config,

1242 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

1243 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

1244{

1245 return [spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)(dev, config, tx\_bufs, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), sig);

1246}

1247

1248#endif /\* CONFIG\_POLL \*/

1249

1251#endif /\* CONFIG\_SPI\_ASYNC \*/

1252

1253

1254#if defined(CONFIG\_SPI\_RTIO) || defined(\_\_DOXYGEN\_\_)

1255

[ 1270](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)static inline void [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1271{

1272 const struct [spi\_dt\_spec](structspi__dt__spec.md) \*dt\_spec = (const struct [spi\_dt\_spec](structspi__dt__spec.md) \*)iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1273 const struct [device](structdevice.md) \*dev = dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a);

1274 const struct [spi\_driver\_api](structspi__driver__api.md) \*api = (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1275

1276 api->iodev\_submit(dt\_spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), iodev\_sqe);

1277}

1278

1280extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) spi\_iodev\_api;

1282

[ 1294](group__spi__interface.md#ga1e9f5fe389d53c280639f23ea134e18c)#define SPI\_DT\_IODEV\_DEFINE(name, node\_id, operation\_, delay\_) \

1295 const struct spi\_dt\_spec \_spi\_dt\_spec\_##name = \

1296 SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_); \

1297 RTIO\_IODEV\_DEFINE(name, &spi\_iodev\_api, (void \*)&\_spi\_dt\_spec\_##name)

1298

[ 1307](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)static inline bool [spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)(const struct [rtio\_iodev](structrtio__iodev.md) \*spi\_iodev)

1308{

1309 struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec = (struct [spi\_dt\_spec](structspi__dt__spec.md) \*)spi\_iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1310

1311 return [spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)(spec);

1312}

1313

1314

1315#endif /\* CONFIG\_SPI\_RTIO \*/

1316

[ 1337](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)\_\_syscall int [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(const struct [device](structdevice.md) \*dev,

1338 const struct [spi\_config](structspi__config.md) \*[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1339

1340static inline int z\_impl\_spi\_release(const struct [device](structdevice.md) \*dev,

1341 const struct [spi\_config](structspi__config.md) \*[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e))

1342{

1343 const struct [spi\_driver\_api](structspi__driver__api.md) \*api =

1344 (const struct [spi\_driver\_api](structspi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1345

1346 return api->release(dev, config);

1347}

1348

[ 1360](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)static inline int [spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)(const struct [spi\_dt\_spec](structspi__dt__spec.md) \*spec)

1361{

1362 return [spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)(spec->[bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a), &spec->[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e));

1363}

1364

1365#ifdef \_\_cplusplus

1366}

1367#endif

1368

1372

1373#include <zephyr/syscalls/spi.h>

1374

1378#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SPI\_H\_ \*/

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

**Definition** gpio.h:837

[spi\_api\_io\_async](group__spi__interface.md#ga03be7f33032ac479153616bbe26848e7)

int(\* spi\_api\_io\_async)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t cb, void \*userdata)

**Definition** spi.h:814

[spi\_release](group__spi__interface.md#ga0c4f4f0a93bb83a4f58d551a7491164e)

int spi\_release(const struct device \*dev, const struct spi\_config \*config)

Release the SPI device locked on and/or the CS by the current config.

[spi\_callback\_t](group__spi__interface.md#ga1db2a410f482d0f26c49f96352aa606d)

void(\* spi\_callback\_t)(const struct device \*dev, int result, void \*data)

SPI callback for asynchronous transfer requests.

**Definition** spi.h:807

[spi\_write\_dt](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)

static int spi\_write\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs)

Write data to a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:1064

[spi\_is\_ready\_dt](group__spi__interface.md#ga37b4e5079ed18b70b0c5a260f4c36403)

static bool spi\_is\_ready\_dt(const struct spi\_dt\_spec \*spec)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:887

[spi\_operation\_t](group__spi__interface.md#ga398a8ae1c4799e77fb6c067b6d47294a)

uint16\_t spi\_operation\_t

Opaque type to hold the SPI operation flags.

**Definition** spi.h:380

[spi\_api\_io](group__spi__interface.md#ga3fc669f866b03cfdad98754de69cda13)

int(\* spi\_api\_io)(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Callback API for I/O See spi\_transceive() for argument descriptions.

**Definition** spi.h:795

[spi\_transceive\_signal](group__spi__interface.md#ga41b8a541257c0d45575fdc4593417edc)

static int spi\_transceive\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:1166

[spi\_read](group__spi__interface.md#ga41f771785a4fa9ca0954125d1e97959e)

static int spi\_read(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:1001

[spi\_transceive\_dt](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff)

static int spi\_transceive\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write data from an SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:974

[spi\_transceive\_cb](group__spi__interface.md#ga6114e63ca23b82f9be0ac70e372b878b)

static int spi\_transceive\_cb(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, spi\_callback\_t callback, void \*userdata)

Read/write the specified amount of data from the SPI driver.

**Definition** spi.h:1116

[SPI\_STATS\_TRANSFER\_ERROR\_INC](group__spi__interface.md#ga6f69e68a79afbbe016aecc515f14de3a)

#define SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

**Definition** spi.h:738

[spi\_read\_dt](group__spi__interface.md#ga7a1d7ebd37d2861b169c265cb90015bf)

static int spi\_read\_dt(const struct spi\_dt\_spec \*spec, const struct spi\_buf\_set \*rx\_bufs)

Read data from a SPI bus specified in spi\_dt\_spec.

**Definition** spi.h:1020

[spi\_write](group__spi__interface.md#ga7e7c4460670ec1c0433ba19accd97796)

static int spi\_write(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:1045

[spi\_release\_dt](group__spi__interface.md#ga829b59767c51b20b546eee8a9cc84b69)

static int spi\_release\_dt(const struct spi\_dt\_spec \*spec)

Release the SPI device specified in spi\_dt\_spec.

**Definition** spi.h:1360

[spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b)

static void spi\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit a SPI device with a request.

**Definition** spi.h:1270

[spi\_read\_signal](group__spi__interface.md#ga9a1ceadb217368232af5b688c12169c5)

static int spi\_read\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*rx\_bufs, struct k\_poll\_signal \*sig)

Read the specified amount of data from the SPI driver.

**Definition** spi.h:1206

[spi\_cs\_is\_gpio\_dt](group__spi__interface.md#gaa13f0da1f28cffa0da4677987db0c9c5)

static bool spi\_cs\_is\_gpio\_dt(const struct spi\_dt\_spec \*spec)

Check if SPI CS in spi\_dt\_spec is controlled using a GPIO.

**Definition** spi.h:874

[spi\_api\_release](group__spi__interface.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)

int(\* spi\_api\_release)(const struct device \*dev, const struct spi\_config \*config)

Callback API for unlocking SPI device.

**Definition** spi.h:836

[spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5)

int spi\_transceive(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Read/write the specified amount of data from the SPI driver.

[spi\_transceive\_stats](group__spi__interface.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)

#define spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

**Definition** spi.h:740

[spi\_write\_signal](group__spi__interface.md#gadcb19d43461ef88e31f6b382cc87fd0b)

static int spi\_write\_signal(const struct device \*dev, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, struct k\_poll\_signal \*sig)

Write the specified amount of data from the SPI driver.

**Definition** spi.h:1240

[spi\_cs\_is\_gpio](group__spi__interface.md#gae1156a4ee1b5909c321811045566d888)

static bool spi\_cs\_is\_gpio(const struct spi\_config \*config)

Check if SPI CS is controlled using a GPIO.

**Definition** spi.h:862

[spi\_is\_ready\_iodev](group__spi__interface.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)

static bool spi\_is\_ready\_iodev(const struct rtio\_iodev \*spi\_iodev)

Validate that SPI bus (and CS gpio if defined) is ready.

**Definition** spi.h:1307

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

**Definition** device.h:455

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:520

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:289

[gpio\_dt\_spec::port](structgpio__dt__spec.md#a5d617d47e2f568c7a4402a8f5a40ed4f)

const struct device \* port

GPIO device controlling the pin.

**Definition** gpio.h:291

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:6122

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:524

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:514

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:515

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:539

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:544

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:304

[spi\_buf\_set](structspi__buf__set.md)

SPI scatter-gather buffer array structure.

**Definition** spi.h:570

[spi\_buf\_set::buffers](structspi__buf__set.md#a2b88917ca29487b2d0b5b63d2083db67)

const struct spi\_buf \* buffers

Pointer to an array of spi\_buf, or NULL.

**Definition** spi.h:572

[spi\_buf\_set::count](structspi__buf__set.md#abc7c37cffebb7873aaba2e524c9a23dc)

size\_t count

Number of buffers in the array pointed to: by buffers.

**Definition** spi.h:574

[spi\_buf](structspi__buf.md)

SPI buffer structure.

**Definition** spi.h:552

[spi\_buf::len](structspi__buf.md#a9755deadff0dd01a886f22e41099b8ba)

size\_t len

Length of the buffer buf in bytes, or length of NOP.

**Definition** spi.h:556

[spi\_buf::buf](structspi__buf.md#aeaf52d3ff5af10545b2d6904ed452cba)

void \* buf

Valid pointer to a data buffer, or NULL for NOP indication.

**Definition** spi.h:554

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:390

[spi\_config::slave](structspi__config.md#a020ca853537483b9641c37be70ab6ca0)

uint16\_t slave

Slave number from 0 to host controller slave limit.

**Definition** spi.h:415

[spi\_config::cs](structspi__config.md#a537dbfe323fafedaa219de1be2097dde)

struct spi\_cs\_control cs

GPIO chip-select line (optional, must be initialized to zero if not used).

**Definition** spi.h:420

[spi\_config::operation](structspi__config.md#a71a02ea548e187e6511abf10fdfa4829)

spi\_operation\_t operation

Operation flags.

**Definition** spi.h:413

[spi\_config::frequency](structspi__config.md#aa1ec6933fe66f91653c5be488e4c9b2a)

uint32\_t frequency

Bus frequency in Hertz.

**Definition** spi.h:392

[spi\_cs\_control](structspi__cs__control.md)

SPI Chip Select control structure.

**Definition** spi.h:242

[spi\_cs\_control::delay](structspi__cs__control.md#a04569d78ac7d6022ffee0c28f5d3b629)

uint32\_t delay

Delay in microseconds to wait before starting the transmission and before releasing the CS line.

**Definition** spi.h:255

[spi\_cs\_control::gpio](structspi__cs__control.md#a8ad907e168666c2ddca77e89f9b9f47f)

struct gpio\_dt\_spec gpio

GPIO devicetree specification of CS GPIO.

**Definition** spi.h:250

[spi\_driver\_api](structspi__driver__api.md)

SPI driver API This is the mandatory API any SPI driver needs to expose.

**Definition** spi.h:844

[spi\_driver\_api::transceive](structspi__driver__api.md#abeb852d35e4772dcec716cf63ef307bb)

spi\_api\_io transceive

**Definition** spi.h:845

[spi\_driver\_api::release](structspi__driver__api.md#ae15944912ece9f736fd935184e8a184d)

spi\_api\_release release

**Definition** spi.h:852

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:466

[spi\_dt\_spec::bus](structspi__dt__spec.md#a37519633ae787ffaa1026e6867d7007a)

const struct device \* bus

SPI bus.

**Definition** spi.h:468

[spi\_dt\_spec::config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e)

struct spi\_config config

Slave specific configuration.

**Definition** spi.h:470

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi.h](drivers_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
