---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/device_8h_source.html
original_path: doxygen/html/device_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device.h

[Go to the documentation of this file.](device_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEVICE\_H\_

8#define ZEPHYR\_INCLUDE\_DEVICE\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/devicetree.h](devicetree_8h.md)>

13#include <[zephyr/init.h](init_8h.md)>

14#include <[zephyr/linker/sections.h](sections_8h.md)>

15#include <[zephyr/pm/state.h](state_8h.md)>

16#include <[zephyr/sys/device\_mmio.h](device__mmio_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18#include <[zephyr/sys/util.h](sys_2util_8h.md)>

19#include <[zephyr/toolchain.h](toolchain_8h.md)>

20

21#ifdef CONFIG\_LLEXT

22#include <[zephyr/llext/symbol.h](symbol_8h.md)>

23#endif

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

36

38

43#define Z\_DEVICE\_DEPS\_SEP INT16\_MIN

44

49#define Z\_DEVICE\_DEPS\_ENDS INT16\_MAX

50

52#define Z\_DEVICE\_IS\_MUTABLE(node\_id) \

53 COND\_CODE\_1(IS\_ENABLED(CONFIG\_DEVICE\_MUTABLE), (DT\_PROP(node\_id, zephyr\_mutable)), (0))

54

56

[ 72](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3);

73

[ 75](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)#define DEVICE\_HANDLE\_NULL 0

76

[ 96](group__device__model.md#ga430eb7530aeb3cff5708b55f9b571eb9)#define DEVICE\_NAME\_GET(dev\_id) \_CONCAT(\_\_device\_, dev\_id)

97

98/\* This macro synthesizes a unique dev\_id from a devicetree node by using

99 \* the node's dependency ordinal.

100 \*

101 \* The ordinal used in this name can be mapped to the path by

102 \* examining zephyr/include/generated/zephyr/devicetree\_generated.h.

103 \*/

104#define Z\_DEVICE\_DT\_DEP\_ORD(node\_id) \_CONCAT(dts\_ord\_, DT\_DEP\_ORD(node\_id))

105

106/\* Same as above, but uses the hash of the node path instead of the ordinal.

107 \*

108 \* The hash used in this name can be mapped to the path by

109 \* examining zephyr/include/generated/zephyr/devicetree\_generated.h.

110 \*/

111#define Z\_DEVICE\_DT\_HASH(node\_id) \_CONCAT(dts\_, DT\_NODE\_HASH(node\_id))

112

113/\* By default, device identifiers are obtained using the dependency ordinal.

114 \* When LLEXT\_EXPORT\_DEV\_IDS\_BY\_HASH is defined, the main Zephyr binary exports

115 \* DT identifiers via EXPORT\_SYMBOL\_NAMED as hashed versions of their paths.

116 \* When matching extensions are built, that is what they need to look for.

117 \*

118 \* The ordinal or hash used in this name can be mapped to the path by

119 \* examining zephyr/include/generated/zephyr/devicetree\_generated.h.

120 \*/

121#if defined(LL\_EXTENSION\_BUILD) && defined(CONFIG\_LLEXT\_EXPORT\_DEV\_IDS\_BY\_HASH)

122#define Z\_DEVICE\_DT\_DEV\_ID(node\_id) Z\_DEVICE\_DT\_HASH(node\_id)

123#else

124#define Z\_DEVICE\_DT\_DEV\_ID(node\_id) Z\_DEVICE\_DT\_DEP\_ORD(node\_id)

125#endif

126

127#if defined(CONFIG\_LLEXT\_EXPORT\_DEV\_IDS\_BY\_HASH)

128/\* Export device identifiers by hash \*/

129#define Z\_DEVICE\_EXPORT(node\_id) \

130 EXPORT\_SYMBOL\_NAMED(DEVICE\_DT\_NAME\_GET(node\_id), \

131 DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_HASH(node\_id)))

132#elif defined(CONFIG\_LLEXT\_EXPORT\_DEVICES)

133/\* Export device identifiers using the builtin name \*/

134#define Z\_DEVICE\_EXPORT(node\_id) EXPORT\_SYMBOL(DEVICE\_DT\_NAME\_GET(node\_id))

135#endif

136

[ 173](group__device__model.md#ga61d851f960a701c9d47d6167b35ac99c)#define DEVICE\_DEINIT\_DEFINE(dev\_id, name, init\_fn, deinit\_fn, pm, data, \

174 config, level, prio, api) \

175 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

176 Z\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, name, init\_fn, deinit\_fn, 0U, \

177 pm, data, config, level, prio, api, \

178 &Z\_DEVICE\_STATE\_NAME(dev\_id))

179

[ 185](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)#define DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, \

186 api) \

187 DEVICE\_DEINIT\_DEFINE(dev\_id, name, init\_fn, NULL, pm, data, config, \

188 level, prio, api)

189

[ 201](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)#define DEVICE\_DT\_NAME(node\_id) \

202 DT\_PROP\_OR(node\_id, label, DT\_NODE\_FULL\_NAME(node\_id))

203

[ 240](group__device__model.md#gaa53f7267950569df898b0e5362e6f583)#define DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, deinit\_fn, pm, data, config, \

241 level, prio, api, ...) \

242 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

243 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

244 DEVICE\_DT\_NAME(node\_id), init\_fn, deinit\_fn, \

245 Z\_DEVICE\_DT\_FLAGS(node\_id), pm, data, config, level, \

246 prio, api, \

247 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

248 \_\_VA\_ARGS\_\_)

249

[ 256](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, \

257 ...) \

258 DEVICE\_DT\_DEINIT\_DEFINE(node\_id, init\_fn, NULL, pm, data, config, \

259 level, prio, api, \_\_VA\_ARGS\_\_)

260

[ 269](group__device__model.md#ga85eecc663e60efa947a59844bcb0bb54)#define DEVICE\_DT\_INST\_DEINIT\_DEFINE(inst, ...) \

270 DEVICE\_DT\_DEINIT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

271

[ 280](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)#define DEVICE\_DT\_INST\_DEFINE(inst, ...) \

281 DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

282

[ 297](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)#define DEVICE\_DT\_NAME\_GET(node\_id) DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

298

[ 314](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)#define DEVICE\_DT\_GET(node\_id) (&DEVICE\_DT\_NAME\_GET(node\_id))

315

[ 325](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)#define DEVICE\_DT\_INST\_GET(inst) DEVICE\_DT\_GET(DT\_DRV\_INST(inst))

326

[ 343](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)#define DEVICE\_DT\_GET\_ANY(compat) \

344 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

345 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

346 (NULL))

347

[ 364](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)#define DEVICE\_DT\_GET\_ONE(compat) \

365 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

366 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

367 (ZERO\_OR\_COMPILE\_ERROR(0)))

368

[ 379](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)#define DEVICE\_DT\_GET\_OR\_NULL(node\_id) \

380 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS\_OKAY(node\_id), \

381 (DEVICE\_DT\_GET(node\_id)), (NULL))

382

[ 396](group__device__model.md#ga7abe347d0aa972e15d1f35af02265a6b)#define DEVICE\_DT\_GET\_BY\_IDX(node\_id, prop, idx) \

397 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx))

398

[ 409](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)#define DEVICE\_GET(dev\_id) (&DEVICE\_NAME\_GET(dev\_id))

410

[ 425](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)#define DEVICE\_DECLARE(dev\_id) \

426 static const struct device DEVICE\_NAME\_GET(dev\_id)

427

[ 435](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)#define DEVICE\_INIT\_DT\_GET(node\_id) \

436 (&Z\_INIT\_ENTRY\_NAME(DEVICE\_DT\_NAME\_GET(node\_id)))

437

[ 445](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)#define DEVICE\_INIT\_GET(dev\_id) (&Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)))

446

[ 455](structdevice__state.md)struct [device\_state](structdevice__state.md) {

[ 463](structdevice__state.md#a4895f511a9246d27a378253ab82e263e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e);

464

[ 468](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) bool [initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) : 1;

469};

470

471struct [pm\_device\_base](structpm__device__base.md);

472struct [pm\_device](structpm__device.md);

473struct [pm\_device\_isr](structpm__device__isr.md);

474#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

475struct device\_dt\_metadata;

476#endif

477

478#ifdef CONFIG\_DEVICE\_DEPS\_DYNAMIC

479#define Z\_DEVICE\_DEPS\_CONST

480#else

481#define Z\_DEVICE\_DEPS\_CONST const

482#endif

483

[ 485](group__device__model.md#gae3daac2d0f7f881d15e47fa15009f15b)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_flags\_t](group__device__model.md#gae3daac2d0f7f881d15e47fa15009f15b);

486

491

[ 493](group__device__model.md#ga9541cb57fcd27619621668e4034d034d)#define DEVICE\_FLAG\_INIT\_DEFERRED BIT(0)

494

496

[ 498](structdevice__ops.md)struct [device\_ops](structdevice__ops.md) {

[ 500](structdevice__ops.md#a28b38a3b3d56f3f29ec379157e9f7e15) int (\*[init](structdevice__ops.md#a28b38a3b3d56f3f29ec379157e9f7e15))(const struct [device](structdevice.md) \*dev);

501#ifdef CONFIG\_DEVICE\_DEINIT\_SUPPORT

503 int (\*deinit)(const struct [device](structdevice.md) \*dev);

504#endif /\* CONFIG\_DEVICE\_DEINIT\_SUPPORT \*/

505};

506

[ 510](structdevice.md)struct [device](structdevice.md) {

[ 512](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d) const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d);

[ 514](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc) const void \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

[ 516](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) const void \*[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

[ 518](structdevice.md#abe18f600adc4ab760963928477cc944e) struct [device\_state](structdevice__state.md) \*[state](structdevice.md#abe18f600adc4ab760963928477cc944e);

[ 520](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e) void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

[ 522](structdevice.md#ab6d65f3402e67afb9810a8356b915071) struct [device\_ops](structdevice__ops.md) [ops](structdevice.md#ab6d65f3402e67afb9810a8356b915071);

[ 524](structdevice.md#ab0854b892499803daf66de8519cc3ff5) [device\_flags\_t](group__device__model.md#gae3daac2d0f7f881d15e47fa15009f15b) [flags](structdevice.md#ab0854b892499803daf66de8519cc3ff5);

525#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

[ 534](structdevice.md#a1452f3badd041e8eccf726756700e8fe) Z\_DEVICE\_DEPS\_CONST [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

535#endif /\* CONFIG\_DEVICE\_DEPS \*/

536#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

541 union {

[ 542](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99) struct [pm\_device\_base](structpm__device__base.md) \*[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

[ 543](structdevice.md#a204619a873db1b99ea31f1c190760052) struct [pm\_device](structpm__device.md) \*[pm](structdevice.md#a204619a873db1b99ea31f1c190760052);

[ 544](structdevice.md#a1526ad6d863e16287de8f06dff7164dc) struct [pm\_device\_isr](structpm__device__isr.md) \*[pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc);

545 };

546#endif

547#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

[ 548](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) const struct device\_dt\_metadata \*[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba);

549#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

550};

551

[ 560](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)static inline [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)(const struct [device](structdevice.md) \*dev)

561{

562 [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) ret = [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0);

563 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

564

565 /\* TODO: If/when devices can be constructed that are not part of the

566 \* fixed sequence we'll need another solution.

567 \*/

568 if (dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

569 ret = 1 + ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3))(dev - [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md)));

570 }

571

572 return ret;

573}

574

583static inline const struct [device](structdevice.md) \*

[ 584](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle)

585{

586 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

587 const struct [device](structdevice.md) \*dev = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

588 size\_t numdev;

589

590 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([device](structdevice.md), &numdev);

591

592 if ((dev\_handle > 0) && ((size\_t)dev\_handle <= numdev)) {

593 dev = &[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md))[dev\_handle - 1];

594 }

595

596 return dev;

597}

598

599#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

600

[ 619](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)typedef int (\*[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb))(const struct [device](structdevice.md) \*dev,

620 void \*context);

621

640static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 641](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)(const struct [device](structdevice.md) \*dev, size\_t \*count)

642{

643 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

644

645 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

646 size\_t i = 0;

647

648 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

649 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

650 ++i;

651 }

652 \*count = i;

653 }

654

655 return rv;

656}

657

676static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 677](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)(const struct [device](structdevice.md) \*dev, size\_t \*count)

678{

679 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

680 size\_t region = 0;

681 size\_t i = 0;

682

683 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

684 /\* Fast forward to injected devices \*/

685 while (region != 1) {

686 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

687 region++;

688 }

689 rv++;

690 }

691 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

692 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

693 ++i;

694 }

695 \*count = i;

696 }

697

698 return rv;

699}

700

720static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 721](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)(const struct [device](structdevice.md) \*dev, size\_t \*count)

722{

723 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

724 size\_t region = 0;

725 size\_t i = 0;

726

727 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

728 /\* Fast forward to supporting devices \*/

729 while (region != 2) {

730 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

731 region++;

732 }

733 rv++;

734 }

735 /\* Count supporting devices.

736 \* Trailing NULL's can be injected by gen\_device\_deps.py due to

737 \* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN\_DYNAMIC\_NUM

738 \*/

739 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

740 (rv[i] != [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0))) {

741 ++i;

742 }

743 \*count = i;

744 }

745

746 return rv;

747}

748

[ 779](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)int [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)(const struct [device](structdevice.md) \*dev,

780 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

781 void \*context);

782

[ 812](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)int [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)(const struct [device](structdevice.md) \*dev,

813 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

814 void \*context);

815

816#endif /\* CONFIG\_DEVICE\_DEPS \*/

817

[ 838](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)\_\_syscall const struct [device](structdevice.md) \*[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

839

848size\_t z\_device\_get\_all\_static(const struct [device](structdevice.md) \*\*devices);

849

[ 866](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)\_\_syscall bool [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(const struct [device](structdevice.md) \*dev);

867

[ 881](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)\_\_syscall int [device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)(const struct [device](structdevice.md) \*dev);

882

[ 903](group__device__model.md#ga73c949c90a7434a7ad31dc9047166417)\_\_syscall int [device\_deinit](group__device__model.md#ga73c949c90a7434a7ad31dc9047166417)(const struct [device](structdevice.md) \*dev);

904

908

910

915#define Z\_DEVICE\_STATE\_NAME(dev\_id) \_CONCAT(\_\_devstate\_, dev\_id)

916

922#define Z\_DEVICE\_STATE\_DEFINE(dev\_id) \

923 static Z\_DECL\_ALIGN(struct device\_state) Z\_DEVICE\_STATE\_NAME(dev\_id) \

924 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

925

931#define Z\_DEVICE\_DT\_FLAGS(node\_id) \

932 (DT\_PROP\_OR(node\_id, zephyr\_deferred\_init, 0U) \* DEVICE\_FLAG\_INIT\_DEFERRED)

933

934#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

935

942#define Z\_DEVICE\_DEPS\_NAME(dev\_id) \_CONCAT(\_\_devicedeps\_, dev\_id)

943

949#define Z\_DEVICE\_EXTRA\_DEPS(...) \

950 FOR\_EACH\_NONEMPTY\_TERM(IDENTITY, (,), \_\_VA\_ARGS\_\_)

951

953#define Z\_DEVICE\_DEPS\_SECTION \

954 \_\_attribute\_\_((\_\_section\_\_(".\_\_device\_deps\_pass1")))

955

956#ifdef \_\_cplusplus

957#define Z\_DEVICE\_DEPS\_EXTERN extern

958#else

959#define Z\_DEVICE\_DEPS\_EXTERN

960#endif

961

997#define Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, ...) \

998 extern Z\_DEVICE\_DEPS\_CONST device\_handle\_t Z\_DEVICE\_DEPS\_NAME( \

999 dev\_id)[]; \

1000 Z\_DEVICE\_DEPS\_CONST Z\_DECL\_ALIGN(device\_handle\_t) \

1001 Z\_DEVICE\_DEPS\_SECTION Z\_DEVICE\_DEPS\_EXTERN \_\_weak \

1002 Z\_DEVICE\_DEPS\_NAME(dev\_id)[] = { \

1003 COND\_CODE\_1( \

1004 DT\_NODE\_EXISTS(node\_id), \

1005 (DT\_DEP\_ORD(node\_id), DT\_REQUIRES\_DEP\_ORDS(node\_id)), \

1006 (DEVICE\_HANDLE\_NULL,)) /\*\*/ \

1007 Z\_DEVICE\_DEPS\_SEP, \

1008 Z\_DEVICE\_EXTRA\_DEPS(\_\_VA\_ARGS\_\_) /\*\*/ \

1009 Z\_DEVICE\_DEPS\_SEP, \

1010 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

1011 (DT\_SUPPORTS\_DEP\_ORDS(node\_id)), ()) /\*\*/ \

1012 }

1013

1014#endif /\* CONFIG\_DEVICE\_DEPS \*/

1015#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

1019struct device\_dt\_nodelabels {

1020 /\* @brief number of elements in the nodelabels array \*/

1021 size\_t num\_nodelabels;

1022 /\* @brief array of node labels as strings, exactly as they

1023 \* appear in the final devicetree

1024 \*/

1025 const char \*nodelabels[];

1026};

1027

1035struct device\_dt\_metadata {

1040 const struct device\_dt\_nodelabels \*nl;

1041};

1042

1061\_\_syscall const struct [device](structdevice.md) \*device\_get\_by\_dt\_nodelabel(const char \*nodelabel);

1062

1068static inline const struct device\_dt\_nodelabels \*

1069device\_get\_dt\_nodelabels(const struct [device](structdevice.md) \*dev)

1070{

1071 if (dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1072 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1073 }

1074 return dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)->nl;

1075}

1076

1083#define Z\_DEVICE\_MAX\_NODELABEL\_LEN Z\_DEVICE\_MAX\_NAME\_LEN

1084

1089#define Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_meta\_, dev\_id)

1090

1095#define Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_nodelabels\_, dev\_id)

1096

1103#define Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id) \

1104 static const struct device\_dt\_nodelabels \

1105 Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) = { \

1106 .num\_nodelabels = DT\_NUM\_NODELABELS(node\_id), \

1107 .nodelabels = DT\_NODELABEL\_STRING\_ARRAY(node\_id), \

1108 }; \

1109 \

1110 static const struct device\_dt\_metadata \

1111 Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) = { \

1112 .nl = &Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id), \

1113 };

1114#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

1115

1123#define Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id) \

1124 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

1125 (DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)), (0))

1126

1133#define Z\_DEVICE\_MAX\_NAME\_LEN 48U

1134

1140#define Z\_DEVICE\_NAME\_CHECK(name) \

1141 BUILD\_ASSERT(sizeof(Z\_STRINGIFY(name)) <= Z\_DEVICE\_MAX\_NAME\_LEN, \

1142 Z\_STRINGIFY(name) " too long")

1143

1150#define Z\_DEVICE\_OPS(init\_fn\_, deinit\_fn\_) \

1151 { \

1152 .init = (init\_fn\_), \

1153 IF\_ENABLED(CONFIG\_DEVICE\_DEINIT\_SUPPORT, \

1154 (.deinit = (deinit\_fn\_),)) \

1155 }

1156

1173#define Z\_DEVICE\_INIT(name\_, init\_fn\_, deinit\_fn\_, flags\_, pm\_, data\_, config\_, api\_, \

1174 state\_, deps\_, node\_id\_, dev\_id\_) \

1175 { \

1176 .name = name\_, \

1177 .config = (config\_), \

1178 .api = (api\_), \

1179 .state = (state\_), \

1180 .data = (data\_), \

1181 .ops = Z\_DEVICE\_OPS(init\_fn\_, deinit\_fn\_), \

1182 .flags = (flags\_), \

1183 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, (.deps = (deps\_),)) /\*\*/ \

1184 IF\_ENABLED(CONFIG\_PM\_DEVICE, Z\_DEVICE\_INIT\_PM\_BASE(pm\_)) /\*\*/ \

1185 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1186 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id\_), \

1187 (.dt\_meta = &Z\_DEVICE\_DT\_METADATA\_NAME\_GET( \

1188 dev\_id\_),)))) \

1189 }

1190

1191/\*

1192 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1193 \* unions but they require these braces when combined with C99 designated initializers. For

1194 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1195 \*/

1196#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1197# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) ({ .pm\_base = (pm\_),},)

1198#else

1199# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) (.pm\_base = (pm\_),)

1200#endif

1201

1208#define Z\_DEVICE\_SECTION\_NAME(level, prio) \

1209 \_CONCAT(INIT\_LEVEL\_ORD(level), \_##prio)

1210

1230#define Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, init\_fn, deinit\_fn, flags, pm, data, config, \

1231 level, prio, api, state, deps) \

1232 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), (), (static)) \

1233 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), (const)) \

1234 STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE( \

1235 device, COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (device\_mutable), (device)), \

1236 Z\_DEVICE\_SECTION\_NAME(level, prio), DEVICE\_NAME\_GET(dev\_id)) = \

1237 Z\_DEVICE\_INIT(name, init\_fn, deinit\_fn, flags, pm, data, config, api, state, deps, \

1238 node\_id, dev\_id)

1239

1245#define Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1246 COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (), \

1247 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (), \

1248 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (), \

1249 (ZERO\_OR\_COMPILE\_ERROR(0)))))))

1250

1260#define Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, level, prio) \

1261 Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1262 \

1263 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan Z\_INIT\_ENTRY\_SECTION( \

1264 level, prio, Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id)) \

1265 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1266 .init\_fn = NULL, \

1267 .dev = (const struct device \*)&DEVICE\_NAME\_GET(dev\_id), \

1268 }

1269

1292#define Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, deinit\_fn, flags, pm, \

1293 data, config, level, prio, api, state, ...) \

1294 Z\_DEVICE\_NAME\_CHECK(name); \

1295 \

1296 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, \

1297 (Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, \_\_VA\_ARGS\_\_);)) \

1298 \

1299 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1300 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1301 (Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id);))))\

1302 \

1303 Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, init\_fn, deinit\_fn, flags, \

1304 pm, data, config, level, prio, api, state, \

1305 Z\_DEVICE\_DEPS\_NAME(dev\_id)); \

1306 \

1307 Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, level, prio); \

1308 \

1309 IF\_ENABLED(CONFIG\_LLEXT\_EXPORT\_DEVICES, \

1310 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1311 (Z\_DEVICE\_EXPORT(node\_id);))))

1312

1323#define Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL(node\_id) \

1324 extern COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), \

1325 (const)) struct device DEVICE\_DT\_NAME\_GET(node\_id);

1326

1327[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL)

1328

1329

1330#define Z\_DEVICE\_API\_TYPE(\_class) \_CONCAT(\_class, \_driver\_api)

1331

1333

[ 1340](device_8h.md#aa0cdc799fc0b9c80eb29f989eec86707)#define DEVICE\_API(\_class, \_name) const STRUCT\_SECTION\_ITERABLE(Z\_DEVICE\_API\_TYPE(\_class), \_name)

1341

[ 1350](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)#define DEVICE\_API\_GET(\_class, \_dev) ((const struct Z\_DEVICE\_API\_TYPE(\_class) \*)\_dev->api)

1351

[ 1362](device_8h.md#a48c6030c2e7d1d05ace7c708dda11949)#define DEVICE\_API\_IS(\_class, \_dev) \

1363 ({ \

1364 STRUCT\_SECTION\_START\_EXTERN(Z\_DEVICE\_API\_TYPE(\_class)); \

1365 STRUCT\_SECTION\_END\_EXTERN(Z\_DEVICE\_API\_TYPE(\_class)); \

1366 (DEVICE\_API\_GET(\_class, \_dev) < STRUCT\_SECTION\_END(Z\_DEVICE\_API\_TYPE(\_class)) && \

1367 DEVICE\_API\_GET(\_class, \_dev) >= STRUCT\_SECTION\_START(Z\_DEVICE\_API\_TYPE(\_class))); \

1368 })

1369

1370#ifdef \_\_cplusplus

1371}

1372#endif

1373

1374#include <zephyr/syscalls/device.h>

1375

1376#endif /\* ZEPHYR\_INCLUDE\_DEVICE\_H\_ \*/

[device\_mmio.h](device__mmio_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)

const struct device \* device\_get\_binding(const char \*name)

Get a device reference from its device::name field.

[device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)

int16\_t device\_handle\_t

Type used to represent a "handle" for a device.

**Definition** device.h:72

[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)

static const device\_handle\_t \* device\_required\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for devicetree dependencies of this device.

**Definition** device.h:641

[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)

static const device\_handle\_t \* device\_supported\_handles\_get(const struct device \*dev, size\_t \*count)

Get the set of handles that this device supports.

**Definition** device.h:721

[device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)

static device\_handle\_t device\_handle\_get(const struct device \*dev)

Get the handle for a given device.

**Definition** device.h:560

[DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)

#define DEVICE\_HANDLE\_NULL

Flag value used to identify an unknown device.

**Definition** device.h:75

[device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)

int device\_required\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly requires.

[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)

static const struct device \* device\_from\_handle(device\_handle\_t dev\_handle)

Get the device corresponding to a handle.

**Definition** device.h:584

[device\_deinit](group__device__model.md#ga73c949c90a7434a7ad31dc9047166417)

int device\_deinit(const struct device \*dev)

De-initialize a device.

[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)

int(\* device\_visitor\_callback\_t)(const struct device \*dev, void \*context)

Prototype for functions used when iterating over a set of devices.

**Definition** device.h:619

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[device\_flags\_t](group__device__model.md#gae3daac2d0f7f881d15e47fa15009f15b)

uint8\_t device\_flags\_t

Device flags.

**Definition** device.h:485

[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)

static const device\_handle\_t \* device\_injected\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for injected dependencies of this device.

**Definition** device.h:677

[device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)

int device\_init(const struct device \*dev)

Initialize a device.

[device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)

int device\_supported\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly supports.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:3000

[STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)

#define STRUCT\_SECTION\_START\_EXTERN(struct\_type)

iterable section extern for start symbol for a struct

**Definition** iterable\_sections.h:159

[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)

#define STRUCT\_SECTION\_START(struct\_type)

iterable section start symbol for a struct type

**Definition** iterable\_sections.h:149

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)

#define STRUCT\_SECTION\_COUNT(struct\_type, dst)

Count elements in a section.

**Definition** iterable\_sections.h:291

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[init.h](init_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[state.h](state_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device\_ops](structdevice__ops.md)

Device operations.

**Definition** device.h:498

[device\_ops::init](structdevice__ops.md#a28b38a3b3d56f3f29ec379157e9f7e15)

int(\* init)(const struct device \*dev)

Initialization function.

**Definition** device.h:500

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:455

[device\_state::initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad)

bool initialized

Indicates the device initialization function has been invoked.

**Definition** device.h:468

[device\_state::init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e)

uint8\_t init\_res

Device initialization return code (positive errno value).

**Definition** device.h:463

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:542

[device::deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe)

const device\_handle\_t \* deps

Optional pointer to dependencies associated with the device.

**Definition** device.h:534

[device::pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc)

struct pm\_device\_isr \* pm\_isr

**Definition** device.h:544

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:512

[device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052)

struct pm\_device \* pm

**Definition** device.h:543

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:520

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[device::flags](structdevice.md#ab0854b892499803daf66de8519cc3ff5)

device\_flags\_t flags

Device flags.

**Definition** device.h:524

[device::ops](structdevice.md#ab6d65f3402e67afb9810a8356b915071)

struct device\_ops ops

Device operations.

**Definition** device.h:522

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:518

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:514

[device::dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)

const struct device\_dt\_metadata \* dt\_meta

**Definition** device.h:548

[pm\_device\_base](structpm__device__base.md)

Device PM info.

**Definition** device.h:139

[pm\_device\_isr](structpm__device__isr.md)

Runtime PM info for device with synchronous PM.

**Definition** device.h:187

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:163

[symbol.h](symbol_8h.md)

Linkable loadable extension symbol definitions.

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [device.h](device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
