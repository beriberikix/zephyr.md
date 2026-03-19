---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/device_8h_source.html
original_path: doxygen/html/device_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 167](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)#define DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, \

168 api) \

169 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

170 Z\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, data, \

171 config, level, prio, api, \

172 &Z\_DEVICE\_STATE\_NAME(dev\_id))

173

[ 185](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)#define DEVICE\_DT\_NAME(node\_id) \

186 DT\_PROP\_OR(node\_id, label, DT\_NODE\_FULL\_NAME(node\_id))

187

[ 195](group__device__model.md#gae16caf17999906091613325f885103cd)#define DEVICE\_DT\_DEFER(node\_id) \

196 DT\_PROP(node\_id, zephyr\_deferred\_init)

197

[ 229](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, \

230 ...) \

231 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

232 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

233 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

234 level, prio, api, \

235 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

236 \_\_VA\_ARGS\_\_)

237

[ 246](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)#define DEVICE\_DT\_INST\_DEFINE(inst, ...) \

247 DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

248

[ 263](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)#define DEVICE\_DT\_NAME\_GET(node\_id) DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

264

[ 280](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)#define DEVICE\_DT\_GET(node\_id) (&DEVICE\_DT\_NAME\_GET(node\_id))

281

[ 291](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)#define DEVICE\_DT\_INST\_GET(inst) DEVICE\_DT\_GET(DT\_DRV\_INST(inst))

292

[ 309](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)#define DEVICE\_DT\_GET\_ANY(compat) \

310 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

311 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

312 (NULL))

313

[ 330](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)#define DEVICE\_DT\_GET\_ONE(compat) \

331 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

332 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

333 (ZERO\_OR\_COMPILE\_ERROR(0)))

334

[ 345](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)#define DEVICE\_DT\_GET\_OR\_NULL(node\_id) \

346 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS\_OKAY(node\_id), \

347 (DEVICE\_DT\_GET(node\_id)), (NULL))

348

[ 362](group__device__model.md#ga7abe347d0aa972e15d1f35af02265a6b)#define DEVICE\_DT\_GET\_BY\_IDX(node\_id, prop, idx) \

363 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx))

364

[ 375](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)#define DEVICE\_GET(dev\_id) (&DEVICE\_NAME\_GET(dev\_id))

376

[ 391](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)#define DEVICE\_DECLARE(dev\_id) \

392 static const struct device DEVICE\_NAME\_GET(dev\_id)

393

[ 401](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)#define DEVICE\_INIT\_DT\_GET(node\_id) \

402 (&Z\_INIT\_ENTRY\_NAME(DEVICE\_DT\_NAME\_GET(node\_id)))

403

[ 411](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)#define DEVICE\_INIT\_GET(dev\_id) (&Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)))

412

[ 421](structdevice__state.md)struct [device\_state](structdevice__state.md) {

[ 429](structdevice__state.md#a4895f511a9246d27a378253ab82e263e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e);

430

[ 434](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) bool [initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) : 1;

435};

436

437struct [pm\_device\_base](structpm__device__base.md);

438struct [pm\_device](structpm__device.md);

439struct [pm\_device\_isr](structpm__device__isr.md);

440#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

441struct device\_dt\_metadata;

442#endif

443

444#ifdef CONFIG\_DEVICE\_DEPS\_DYNAMIC

445#define Z\_DEVICE\_DEPS\_CONST

446#else

447#define Z\_DEVICE\_DEPS\_CONST const

448#endif

449

[ 453](structdevice.md)struct [device](structdevice.md) {

[ 455](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d) const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d);

[ 457](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc) const void \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

[ 459](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) const void \*[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

[ 461](structdevice.md#abe18f600adc4ab760963928477cc944e) struct [device\_state](structdevice__state.md) \*[state](structdevice.md#abe18f600adc4ab760963928477cc944e);

[ 463](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e) void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

464#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

[ 473](structdevice.md#a1452f3badd041e8eccf726756700e8fe) Z\_DEVICE\_DEPS\_CONST [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

474#endif /\* CONFIG\_DEVICE\_DEPS \*/

475#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

480 union {

[ 481](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99) struct [pm\_device\_base](structpm__device__base.md) \*[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

[ 482](structdevice.md#a204619a873db1b99ea31f1c190760052) struct [pm\_device](structpm__device.md) \*[pm](structdevice.md#a204619a873db1b99ea31f1c190760052);

[ 483](structdevice.md#a1526ad6d863e16287de8f06dff7164dc) struct [pm\_device\_isr](structpm__device__isr.md) \*[pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc);

484 };

485#endif

486#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

[ 487](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) const struct device\_dt\_metadata \*[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba);

488#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

489};

490

[ 499](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)static inline [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)(const struct [device](structdevice.md) \*dev)

500{

501 [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) ret = [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0);

502 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

503

504 /\* TODO: If/when devices can be constructed that are not part of the

505 \* fixed sequence we'll need another solution.

506 \*/

507 if (dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

508 ret = 1 + ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3))(dev - [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md)));

509 }

510

511 return ret;

512}

513

522static inline const struct [device](structdevice.md) \*

[ 523](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle)

524{

525 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

526 const struct [device](structdevice.md) \*dev = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

527 size\_t numdev;

528

529 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([device](structdevice.md), &numdev);

530

531 if ((dev\_handle > 0) && ((size\_t)dev\_handle <= numdev)) {

532 dev = &[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md))[dev\_handle - 1];

533 }

534

535 return dev;

536}

537

538#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

539

[ 558](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)typedef int (\*[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb))(const struct [device](structdevice.md) \*dev,

559 void \*context);

560

579static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 580](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)(const struct [device](structdevice.md) \*dev, size\_t \*count)

581{

582 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

583

584 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

585 size\_t i = 0;

586

587 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

588 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

589 ++i;

590 }

591 \*count = i;

592 }

593

594 return rv;

595}

596

615static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 616](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)(const struct [device](structdevice.md) \*dev, size\_t \*count)

617{

618 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

619 size\_t region = 0;

620 size\_t i = 0;

621

622 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

623 /\* Fast forward to injected devices \*/

624 while (region != 1) {

625 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

626 region++;

627 }

628 rv++;

629 }

630 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

631 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

632 ++i;

633 }

634 \*count = i;

635 }

636

637 return rv;

638}

639

659static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 660](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)(const struct [device](structdevice.md) \*dev, size\_t \*count)

661{

662 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

663 size\_t region = 0;

664 size\_t i = 0;

665

666 if (rv != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

667 /\* Fast forward to supporting devices \*/

668 while (region != 2) {

669 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

670 region++;

671 }

672 rv++;

673 }

674 /\* Count supporting devices.

675 \* Trailing NULL's can be injected by gen\_device\_deps.py due to

676 \* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN\_DYNAMIC\_NUM

677 \*/

678 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

679 (rv[i] != [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0))) {

680 ++i;

681 }

682 \*count = i;

683 }

684

685 return rv;

686}

687

[ 718](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)int [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)(const struct [device](structdevice.md) \*dev,

719 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

720 void \*context);

721

[ 751](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)int [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)(const struct [device](structdevice.md) \*dev,

752 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

753 void \*context);

754

755#endif /\* CONFIG\_DEVICE\_DEPS \*/

756

[ 777](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)\_\_syscall const struct [device](structdevice.md) \*[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

778

787size\_t z\_device\_get\_all\_static(const struct [device](structdevice.md) \*\*devices);

788

[ 805](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)\_\_syscall bool [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(const struct [device](structdevice.md) \*dev);

806

[ 821](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)\_\_syscall int [device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)(const struct [device](structdevice.md) \*dev);

822

826

828

833#define Z\_DEVICE\_STATE\_NAME(dev\_id) \_CONCAT(\_\_devstate\_, dev\_id)

834

840#define Z\_DEVICE\_STATE\_DEFINE(dev\_id) \

841 static Z\_DECL\_ALIGN(struct device\_state) Z\_DEVICE\_STATE\_NAME(dev\_id) \

842 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

843

844#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

845

852#define Z\_DEVICE\_DEPS\_NAME(dev\_id) \_CONCAT(\_\_devicedeps\_, dev\_id)

853

859#define Z\_DEVICE\_EXTRA\_DEPS(...) \

860 FOR\_EACH\_NONEMPTY\_TERM(IDENTITY, (,), \_\_VA\_ARGS\_\_)

861

863#define Z\_DEVICE\_DEPS\_SECTION \

864 \_\_attribute\_\_((\_\_section\_\_(".\_\_device\_deps\_pass1")))

865

866#ifdef \_\_cplusplus

867#define Z\_DEVICE\_DEPS\_EXTERN extern

868#else

869#define Z\_DEVICE\_DEPS\_EXTERN

870#endif

871

907#define Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, ...) \

908 extern Z\_DEVICE\_DEPS\_CONST device\_handle\_t Z\_DEVICE\_DEPS\_NAME( \

909 dev\_id)[]; \

910 Z\_DEVICE\_DEPS\_CONST Z\_DECL\_ALIGN(device\_handle\_t) \

911 Z\_DEVICE\_DEPS\_SECTION Z\_DEVICE\_DEPS\_EXTERN \_\_weak \

912 Z\_DEVICE\_DEPS\_NAME(dev\_id)[] = { \

913 COND\_CODE\_1( \

914 DT\_NODE\_EXISTS(node\_id), \

915 (DT\_DEP\_ORD(node\_id), DT\_REQUIRES\_DEP\_ORDS(node\_id)), \

916 (DEVICE\_HANDLE\_NULL,)) /\*\*/ \

917 Z\_DEVICE\_DEPS\_SEP, \

918 Z\_DEVICE\_EXTRA\_DEPS(\_\_VA\_ARGS\_\_) /\*\*/ \

919 Z\_DEVICE\_DEPS\_SEP, \

920 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

921 (DT\_SUPPORTS\_DEP\_ORDS(node\_id)), ()) /\*\*/ \

922 }

923

924#endif /\* CONFIG\_DEVICE\_DEPS \*/

925#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

929struct device\_dt\_nodelabels {

930 /\* @brief number of elements in the nodelabels array \*/

931 size\_t num\_nodelabels;

932 /\* @brief array of node labels as strings, exactly as they

933 \* appear in the final devicetree

934 \*/

935 const char \*nodelabels[];

936};

937

945struct device\_dt\_metadata {

950 const struct device\_dt\_nodelabels \*nl;

951};

952

971\_\_syscall const struct [device](structdevice.md) \*device\_get\_by\_dt\_nodelabel(const char \*nodelabel);

972

978static inline const struct device\_dt\_nodelabels \*

979device\_get\_dt\_nodelabels(const struct [device](structdevice.md) \*dev)

980{

981 if (dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

982 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

983 }

984 return dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)->nl;

985}

986

993#define Z\_DEVICE\_MAX\_NODELABEL\_LEN Z\_DEVICE\_MAX\_NAME\_LEN

994

999#define Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_meta\_, dev\_id)

1000

1005#define Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_nodelabels\_, dev\_id)

1006

1013#define Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id) \

1014 static const struct device\_dt\_nodelabels \

1015 Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) = { \

1016 .num\_nodelabels = DT\_NUM\_NODELABELS(node\_id), \

1017 .nodelabels = DT\_NODELABEL\_STRING\_ARRAY(node\_id), \

1018 }; \

1019 \

1020 static const struct device\_dt\_metadata \

1021 Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) = { \

1022 .nl = &Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id), \

1023 };

1024#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

1025

1033#define Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id) \

1034 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

1035 (DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)), (0))

1036

1043#define Z\_DEVICE\_MAX\_NAME\_LEN 48U

1044

1050#define Z\_DEVICE\_NAME\_CHECK(name) \

1051 BUILD\_ASSERT(sizeof(Z\_STRINGIFY(name)) <= Z\_DEVICE\_MAX\_NAME\_LEN, \

1052 Z\_STRINGIFY(name) " too long")

1053

1067#define Z\_DEVICE\_INIT(name\_, pm\_, data\_, config\_, api\_, state\_, deps\_, node\_id\_, \

1068 dev\_id\_) \

1069 { \

1070 .name = name\_, \

1071 .config = (config\_), \

1072 .api = (api\_), \

1073 .state = (state\_), \

1074 .data = (data\_), \

1075 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, (.deps = (deps\_),)) /\*\*/ \

1076 IF\_ENABLED(CONFIG\_PM\_DEVICE, Z\_DEVICE\_INIT\_PM\_BASE(pm\_)) /\*\*/ \

1077 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1078 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id\_), \

1079 (.dt\_meta = &Z\_DEVICE\_DT\_METADATA\_NAME\_GET( \

1080 dev\_id\_),)))) \

1081 }

1082

1083/\*

1084 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1085 \* unions but they require these braces when combined with C99 designated initializers. For

1086 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1087 \*/

1088#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1089# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) ({ .pm\_base = (pm\_),},)

1090#else

1091# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) (.pm\_base = (pm\_),)

1092#endif

1093

1100#define Z\_DEVICE\_SECTION\_NAME(level, prio) \

1101 \_CONCAT(INIT\_LEVEL\_ORD(level), \_##prio)

1102

1119#define Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, prio, api, state, \

1120 deps) \

1121 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), (), (static)) \

1122 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), (const)) \

1123 STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE( \

1124 device, COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (device\_mutable), (device)), \

1125 Z\_DEVICE\_SECTION\_NAME(level, prio), DEVICE\_NAME\_GET(dev\_id)) = \

1126 Z\_DEVICE\_INIT(name, pm, data, config, api, state, deps, node\_id, dev\_id)

1127

1133#define Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1134 COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (), \

1135 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (), \

1136 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (), \

1137 (ZERO\_OR\_COMPILE\_ERROR(0)))))))

1138

1149#define Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_, level, prio) \

1150 Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1151 \

1152 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan Z\_INIT\_ENTRY\_SECTION( \

1153 level, prio, Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id)) \

1154 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1155 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1156 (init\_fn\_)}, \

1157 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1158 }

1159

1160#define Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_) \

1161 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan \

1162 \_\_attribute\_\_((\_\_section\_\_(".z\_deferred\_init"))) \

1163 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1164 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1165 (init\_fn\_)}, \

1166 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1167 }

1168

1169/\*

1170 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1171 \* unions but they require these braces when combined with C99 designated initializers. For

1172 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1173 \*/

1174#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1175# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) { Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) }

1176#else

1177# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id)

1178#endif

1179

1180#define Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) \

1181 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = &DEVICE\_NAME\_GET(dev\_id)

1182

1204#define Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, config, \

1205 level, prio, api, state, ...) \

1206 Z\_DEVICE\_NAME\_CHECK(name); \

1207 \

1208 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, \

1209 (Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, \_\_VA\_ARGS\_\_);)) \

1210 \

1211 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1212 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1213 (Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id);))))\

1214 \

1215 Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, \

1216 prio, api, state, Z\_DEVICE\_DEPS\_NAME(dev\_id)); \

1217 COND\_CODE\_1(DEVICE\_DT\_DEFER(node\_id), \

1218 (Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, \

1219 init\_fn)), \

1220 (Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn, \

1221 level, prio))); \

1222 IF\_ENABLED(CONFIG\_LLEXT\_EXPORT\_DEVICES, \

1223 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1224 (Z\_DEVICE\_EXPORT(node\_id);))))

1225

1236#define Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL(node\_id) \

1237 extern COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), \

1238 (const)) struct device DEVICE\_DT\_NAME\_GET(node\_id);

1239

1240[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL)

1241

1242

1243#define Z\_DEVICE\_API\_TYPE(\_class) \_CONCAT(\_class, \_driver\_api)

1244

1246

[ 1253](device_8h.md#aa0cdc799fc0b9c80eb29f989eec86707)#define DEVICE\_API(\_class, \_name) const STRUCT\_SECTION\_ITERABLE(Z\_DEVICE\_API\_TYPE(\_class), \_name)

1254

[ 1263](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)#define DEVICE\_API\_GET(\_class, \_dev) ((const struct Z\_DEVICE\_API\_TYPE(\_class) \*)\_dev->api)

1264

[ 1275](device_8h.md#a48c6030c2e7d1d05ace7c708dda11949)#define DEVICE\_API\_IS(\_class, \_dev) \

1276 ({ \

1277 STRUCT\_SECTION\_START\_EXTERN(Z\_DEVICE\_API\_TYPE(\_class)); \

1278 STRUCT\_SECTION\_END\_EXTERN(Z\_DEVICE\_API\_TYPE(\_class)); \

1279 (DEVICE\_API\_GET(\_class, \_dev) < STRUCT\_SECTION\_END(Z\_DEVICE\_API\_TYPE(\_class)) && \

1280 DEVICE\_API\_GET(\_class, \_dev) >= STRUCT\_SECTION\_START(Z\_DEVICE\_API\_TYPE(\_class))); \

1281 })

1282

1283#ifdef \_\_cplusplus

1284}

1285#endif

1286

1287#include <zephyr/syscalls/device.h>

1288

1289#endif /\* ZEPHYR\_INCLUDE\_DEVICE\_H\_ \*/

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

**Definition** device.h:580

[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)

static const device\_handle\_t \* device\_supported\_handles\_get(const struct device \*dev, size\_t \*count)

Get the set of handles that this device supports.

**Definition** device.h:660

[device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)

static device\_handle\_t device\_handle\_get(const struct device \*dev)

Get the handle for a given device.

**Definition** device.h:499

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

**Definition** device.h:523

[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)

int(\* device\_visitor\_callback\_t)(const struct device \*dev, void \*context)

Prototype for functions used when iterating over a set of devices.

**Definition** device.h:558

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)

static const device\_handle\_t \* device\_injected\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for injected dependencies of this device.

**Definition** device.h:616

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

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:421

[device\_state::initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad)

bool initialized

Indicates the device initialization function has been invoked.

**Definition** device.h:434

[device\_state::init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e)

uint8\_t init\_res

Device initialization return code (positive errno value).

**Definition** device.h:429

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:481

[device::deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe)

const device\_handle\_t \* deps

Optional pointer to dependencies associated with the device.

**Definition** device.h:473

[device::pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc)

struct pm\_device\_isr \* pm\_isr

**Definition** device.h:483

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:455

[device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052)

struct pm\_device \* pm

**Definition** device.h:482

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:461

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:457

[device::dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)

const struct device\_dt\_metadata \* dt\_meta

**Definition** device.h:487

[pm\_device\_base](structpm__device__base.md)

Device PM info.

**Definition** device.h:139

[pm\_device\_isr](structpm__device__isr.md)

Runtime PM info for device with synchronous PM.

**Definition** device.h:185

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
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
