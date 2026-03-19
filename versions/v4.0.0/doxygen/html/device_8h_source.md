---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/device_8h_source.html
original_path: doxygen/html/device_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

104#define Z\_DEVICE\_DT\_DEV\_ID(node\_id) \_CONCAT(dts\_ord\_, DT\_DEP\_ORD(node\_id))

105

106#if defined(CONFIG\_LLEXT\_EXPORT\_DEVICES)

107/\* Export device identifiers using the builtin name \*/

108#define Z\_DEVICE\_EXPORT(node\_id) EXPORT\_SYMBOL(DEVICE\_DT\_NAME\_GET(node\_id))

109#endif

110

[ 141](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)#define DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, \

142 api) \

143 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

144 Z\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, data, \

145 config, level, prio, api, \

146 &Z\_DEVICE\_STATE\_NAME(dev\_id))

147

[ 159](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)#define DEVICE\_DT\_NAME(node\_id) \

160 DT\_PROP\_OR(node\_id, label, DT\_NODE\_FULL\_NAME(node\_id))

161

[ 169](group__device__model.md#gae16caf17999906091613325f885103cd)#define DEVICE\_DT\_DEFER(node\_id) \

170 DT\_PROP(node\_id, zephyr\_deferred\_init)

171

[ 203](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, \

204 ...) \

205 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

206 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

207 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

208 level, prio, api, \

209 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

210 \_\_VA\_ARGS\_\_) \

211 IF\_ENABLED(CONFIG\_LLEXT\_EXPORT\_DEVICES, (Z\_DEVICE\_EXPORT(node\_id);))

212

[ 221](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)#define DEVICE\_DT\_INST\_DEFINE(inst, ...) \

222 DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

223

[ 238](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)#define DEVICE\_DT\_NAME\_GET(node\_id) DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

239

[ 255](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)#define DEVICE\_DT\_GET(node\_id) (&DEVICE\_DT\_NAME\_GET(node\_id))

256

[ 266](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)#define DEVICE\_DT\_INST\_GET(inst) DEVICE\_DT\_GET(DT\_DRV\_INST(inst))

267

[ 284](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)#define DEVICE\_DT\_GET\_ANY(compat) \

285 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

286 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

287 (NULL))

288

[ 305](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)#define DEVICE\_DT\_GET\_ONE(compat) \

306 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

307 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

308 (ZERO\_OR\_COMPILE\_ERROR(0)))

309

[ 320](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)#define DEVICE\_DT\_GET\_OR\_NULL(node\_id) \

321 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS\_OKAY(node\_id), \

322 (DEVICE\_DT\_GET(node\_id)), (NULL))

323

[ 334](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)#define DEVICE\_GET(dev\_id) (&DEVICE\_NAME\_GET(dev\_id))

335

[ 350](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)#define DEVICE\_DECLARE(dev\_id) \

351 static const struct device DEVICE\_NAME\_GET(dev\_id)

352

[ 360](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)#define DEVICE\_INIT\_DT\_GET(node\_id) \

361 (&Z\_INIT\_ENTRY\_NAME(DEVICE\_DT\_NAME\_GET(node\_id)))

362

[ 370](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)#define DEVICE\_INIT\_GET(dev\_id) (&Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)))

371

[ 380](structdevice__state.md)struct [device\_state](structdevice__state.md) {

[ 388](structdevice__state.md#a4895f511a9246d27a378253ab82e263e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e);

389

[ 393](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) bool [initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) : 1;

394};

395

396struct [pm\_device\_base](structpm__device__base.md);

397struct [pm\_device](structpm__device.md);

398struct [pm\_device\_isr](structpm__device__isr.md);

399#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

400struct device\_dt\_metadata;

401#endif

402

403#ifdef CONFIG\_DEVICE\_DEPS\_DYNAMIC

404#define Z\_DEVICE\_DEPS\_CONST

405#else

406#define Z\_DEVICE\_DEPS\_CONST const

407#endif

408

[ 412](structdevice.md)struct [device](structdevice.md) {

[ 414](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d) const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d);

[ 416](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc) const void \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

[ 418](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) const void \*[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

[ 420](structdevice.md#abe18f600adc4ab760963928477cc944e) struct [device\_state](structdevice__state.md) \*[state](structdevice.md#abe18f600adc4ab760963928477cc944e);

[ 422](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e) void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

423#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

[ 432](structdevice.md#a1452f3badd041e8eccf726756700e8fe) Z\_DEVICE\_DEPS\_CONST [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

433#endif /\* CONFIG\_DEVICE\_DEPS \*/

434#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

439 union {

[ 440](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99) struct [pm\_device\_base](structpm__device__base.md) \*[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

[ 441](structdevice.md#a204619a873db1b99ea31f1c190760052) struct [pm\_device](structpm__device.md) \*[pm](structdevice.md#a204619a873db1b99ea31f1c190760052);

[ 442](structdevice.md#a1526ad6d863e16287de8f06dff7164dc) struct [pm\_device\_isr](structpm__device__isr.md) \*[pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc);

443 };

444#endif

445#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

[ 446](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) const struct device\_dt\_metadata \*[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba);

447#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

448};

449

[ 458](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)static inline [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)(const struct [device](structdevice.md) \*dev)

459{

460 [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) ret = [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0);

461 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

462

463 /\* TODO: If/when devices can be constructed that are not part of the

464 \* fixed sequence we'll need another solution.

465 \*/

466 if (dev != NULL) {

467 ret = 1 + ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3))(dev - [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md)));

468 }

469

470 return ret;

471}

472

481static inline const struct [device](structdevice.md) \*

[ 482](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle)

483{

484 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

485 const struct [device](structdevice.md) \*dev = NULL;

486 size\_t numdev;

487

488 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([device](structdevice.md), &numdev);

489

490 if ((dev\_handle > 0) && ((size\_t)dev\_handle <= numdev)) {

491 dev = &[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md))[dev\_handle - 1];

492 }

493

494 return dev;

495}

496

497#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

498

[ 517](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)typedef int (\*[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb))(const struct [device](structdevice.md) \*dev,

518 void \*context);

519

538static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 539](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)(const struct [device](structdevice.md) \*dev, size\_t \*count)

540{

541 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

542

543 if (rv != NULL) {

544 size\_t i = 0;

545

546 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

547 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

548 ++i;

549 }

550 \*count = i;

551 }

552

553 return rv;

554}

555

574static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 575](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)(const struct [device](structdevice.md) \*dev, size\_t \*count)

576{

577 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

578 size\_t region = 0;

579 size\_t i = 0;

580

581 if (rv != NULL) {

582 /\* Fast forward to injected devices \*/

583 while (region != 1) {

584 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

585 region++;

586 }

587 rv++;

588 }

589 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

590 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

591 ++i;

592 }

593 \*count = i;

594 }

595

596 return rv;

597}

598

618static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 619](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)(const struct [device](structdevice.md) \*dev, size\_t \*count)

620{

621 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

622 size\_t region = 0;

623 size\_t i = 0;

624

625 if (rv != NULL) {

626 /\* Fast forward to supporting devices \*/

627 while (region != 2) {

628 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

629 region++;

630 }

631 rv++;

632 }

633 /\* Count supporting devices.

634 \* Trailing NULL's can be injected by gen\_device\_deps.py due to

635 \* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN\_DYNAMIC\_NUM

636 \*/

637 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

638 (rv[i] != [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0))) {

639 ++i;

640 }

641 \*count = i;

642 }

643

644 return rv;

645}

646

[ 677](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)int [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)(const struct [device](structdevice.md) \*dev,

678 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

679 void \*context);

680

[ 710](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)int [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)(const struct [device](structdevice.md) \*dev,

711 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

712 void \*context);

713

714#endif /\* CONFIG\_DEVICE\_DEPS \*/

715

[ 736](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)\_\_syscall const struct [device](structdevice.md) \*[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

737

746size\_t z\_device\_get\_all\_static(const struct [device](structdevice.md) \*\*devices);

747

[ 764](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)\_\_syscall bool [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(const struct [device](structdevice.md) \*dev);

765

[ 780](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)\_\_syscall int [device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)(const struct [device](structdevice.md) \*dev);

781

785

787

792#define Z\_DEVICE\_STATE\_NAME(dev\_id) \_CONCAT(\_\_devstate\_, dev\_id)

793

799#define Z\_DEVICE\_STATE\_DEFINE(dev\_id) \

800 static Z\_DECL\_ALIGN(struct device\_state) Z\_DEVICE\_STATE\_NAME(dev\_id) \

801 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

802

803#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

804

811#define Z\_DEVICE\_DEPS\_NAME(dev\_id) \_CONCAT(\_\_devicedeps\_, dev\_id)

812

818#define Z\_DEVICE\_EXTRA\_DEPS(...) \

819 FOR\_EACH\_NONEMPTY\_TERM(IDENTITY, (,), \_\_VA\_ARGS\_\_)

820

822#define Z\_DEVICE\_DEPS\_SECTION \

823 \_\_attribute\_\_((\_\_section\_\_(".\_\_device\_deps\_pass1")))

824

825#ifdef \_\_cplusplus

826#define Z\_DEVICE\_DEPS\_EXTERN extern

827#else

828#define Z\_DEVICE\_DEPS\_EXTERN

829#endif

830

866#define Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, ...) \

867 extern Z\_DEVICE\_DEPS\_CONST device\_handle\_t Z\_DEVICE\_DEPS\_NAME( \

868 dev\_id)[]; \

869 Z\_DEVICE\_DEPS\_CONST Z\_DECL\_ALIGN(device\_handle\_t) \

870 Z\_DEVICE\_DEPS\_SECTION Z\_DEVICE\_DEPS\_EXTERN \_\_weak \

871 Z\_DEVICE\_DEPS\_NAME(dev\_id)[] = { \

872 COND\_CODE\_1( \

873 DT\_NODE\_EXISTS(node\_id), \

874 (DT\_DEP\_ORD(node\_id), DT\_REQUIRES\_DEP\_ORDS(node\_id)), \

875 (DEVICE\_HANDLE\_NULL,)) /\*\*/ \

876 Z\_DEVICE\_DEPS\_SEP, \

877 Z\_DEVICE\_EXTRA\_DEPS(\_\_VA\_ARGS\_\_) /\*\*/ \

878 Z\_DEVICE\_DEPS\_SEP, \

879 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

880 (DT\_SUPPORTS\_DEP\_ORDS(node\_id)), ()) /\*\*/ \

881 }

882

883#endif /\* CONFIG\_DEVICE\_DEPS \*/

884#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

888struct device\_dt\_nodelabels {

889 /\* @brief number of elements in the nodelabels array \*/

890 size\_t num\_nodelabels;

891 /\* @brief array of node labels as strings, exactly as they

892 \* appear in the final devicetree

893 \*/

894 const char \*nodelabels[];

895};

896

904struct device\_dt\_metadata {

909 const struct device\_dt\_nodelabels \*nl;

910};

911

930\_\_syscall const struct [device](structdevice.md) \*device\_get\_by\_dt\_nodelabel(const char \*nodelabel);

931

937static inline const struct device\_dt\_nodelabels \*

938device\_get\_dt\_nodelabels(const struct [device](structdevice.md) \*dev)

939{

940 if (dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) == NULL) {

941 return NULL;

942 }

943 return dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)->nl;

944}

945

952#define Z\_DEVICE\_MAX\_NODELABEL\_LEN Z\_DEVICE\_MAX\_NAME\_LEN

953

958#define Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_meta\_, dev\_id)

959

964#define Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_nodelabels\_, dev\_id)

965

972#define Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id) \

973 static const struct device\_dt\_nodelabels \

974 Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) = { \

975 .num\_nodelabels = DT\_NUM\_NODELABELS(node\_id), \

976 .nodelabels = DT\_NODELABEL\_STRING\_ARRAY(node\_id), \

977 }; \

978 \

979 static const struct device\_dt\_metadata \

980 Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) = { \

981 .nl = &Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id), \

982 };

983#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

984

992#define Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id) \

993 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

994 (DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)), (0))

995

1002#define Z\_DEVICE\_MAX\_NAME\_LEN 48U

1003

1009#define Z\_DEVICE\_NAME\_CHECK(name) \

1010 BUILD\_ASSERT(sizeof(Z\_STRINGIFY(name)) <= Z\_DEVICE\_MAX\_NAME\_LEN, \

1011 Z\_STRINGIFY(name) " too long")

1012

1026#define Z\_DEVICE\_INIT(name\_, pm\_, data\_, config\_, api\_, state\_, deps\_, node\_id\_, \

1027 dev\_id\_) \

1028 { \

1029 .name = name\_, \

1030 .config = (config\_), \

1031 .api = (api\_), \

1032 .state = (state\_), \

1033 .data = (data\_), \

1034 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, (.deps = (deps\_),)) /\*\*/ \

1035 IF\_ENABLED(CONFIG\_PM\_DEVICE, Z\_DEVICE\_INIT\_PM\_BASE(pm\_)) /\*\*/ \

1036 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1037 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id\_), \

1038 (.dt\_meta = &Z\_DEVICE\_DT\_METADATA\_NAME\_GET( \

1039 dev\_id\_),)))) \

1040 }

1041

1042/\*

1043 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1044 \* unions but they require these braces when combined with C99 designated initializers. For

1045 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1046 \*/

1047#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1048# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) ({ .pm\_base = (pm\_),},)

1049#else

1050# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) (.pm\_base = (pm\_),)

1051#endif

1052

1059#define Z\_DEVICE\_SECTION\_NAME(level, prio) \

1060 \_CONCAT(INIT\_LEVEL\_ORD(level), \_##prio)

1061

1078#define Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, prio, api, state, \

1079 deps) \

1080 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), (), (static)) \

1081 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), (const)) \

1082 STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE( \

1083 device, COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (device\_mutable), (device)), \

1084 Z\_DEVICE\_SECTION\_NAME(level, prio), DEVICE\_NAME\_GET(dev\_id)) = \

1085 Z\_DEVICE\_INIT(name, pm, data, config, api, state, deps, node\_id, dev\_id)

1086

1092#define Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1093 COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (), \

1094 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (), \

1095 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (), \

1096 (ZERO\_OR\_COMPILE\_ERROR(0)))))))

1097

1108#define Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_, level, prio) \

1109 Z\_DEVICE\_CHECK\_INIT\_LEVEL(level) \

1110 \

1111 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan Z\_INIT\_ENTRY\_SECTION( \

1112 level, prio, Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id)) \

1113 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1114 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1115 (init\_fn\_)}, \

1116 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1117 }

1118

1119#define Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_) \

1120 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan \

1121 \_\_attribute\_\_((\_\_section\_\_(".z\_deferred\_init"))) \

1122 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1123 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1124 (init\_fn\_)}, \

1125 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1126 }

1127

1128/\*

1129 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1130 \* unions but they require these braces when combined with C99 designated initializers. For

1131 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1132 \*/

1133#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1134# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) { Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) }

1135#else

1136# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id)

1137#endif

1138

1139#define Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) \

1140 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = &DEVICE\_NAME\_GET(dev\_id)

1141

1163#define Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, config, \

1164 level, prio, api, state, ...) \

1165 Z\_DEVICE\_NAME\_CHECK(name); \

1166 \

1167 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, \

1168 (Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, \_\_VA\_ARGS\_\_);)) \

1169 \

1170 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1171 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1172 (Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id);))))\

1173 \

1174 Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, \

1175 prio, api, state, Z\_DEVICE\_DEPS\_NAME(dev\_id)); \

1176 COND\_CODE\_1(DEVICE\_DT\_DEFER(node\_id), \

1177 (Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, \

1178 init\_fn)), \

1179 (Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn, \

1180 level, prio)));

1181

1192#define Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL(node\_id) \

1193 extern COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), \

1194 (const)) struct device DEVICE\_DT\_NAME\_GET(node\_id);

1195

1196[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL)

1197

1198

1199

1200#ifdef \_\_cplusplus

1201}

1202#endif

1203

1204#include <zephyr/syscalls/device.h>

1205

1206#endif /\* ZEPHYR\_INCLUDE\_DEVICE\_H\_ \*/

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

**Definition** device.h:539

[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)

static const device\_handle\_t \* device\_supported\_handles\_get(const struct device \*dev, size\_t \*count)

Get the set of handles that this device supports.

**Definition** device.h:619

[device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)

static device\_handle\_t device\_handle\_get(const struct device \*dev)

Get the handle for a given device.

**Definition** device.h:458

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

**Definition** device.h:482

[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)

int(\* device\_visitor\_callback\_t)(const struct device \*dev, void \*context)

Prototype for functions used when iterating over a set of devices.

**Definition** device.h:517

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)

static const device\_handle\_t \* device\_injected\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for injected dependencies of this device.

**Definition** device.h:575

[device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)

int device\_init(const struct device \*dev)

Initialize a device.

[device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)

int device\_supported\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly supports.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2942

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

**Definition** device.h:380

[device\_state::initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad)

bool initialized

Indicates the device initialization function has been invoked.

**Definition** device.h:393

[device\_state::init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e)

uint8\_t init\_res

Device initialization return code (positive errno value).

**Definition** device.h:388

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:440

[device::deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe)

const device\_handle\_t \* deps

Optional pointer to dependencies associated with the device.

**Definition** device.h:432

[device::pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc)

struct pm\_device\_isr \* pm\_isr

**Definition** device.h:442

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:414

[device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052)

struct pm\_device \* pm

**Definition** device.h:441

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:420

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:416

[device::dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)

const struct device\_dt\_metadata \* dt\_meta

**Definition** device.h:446

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
