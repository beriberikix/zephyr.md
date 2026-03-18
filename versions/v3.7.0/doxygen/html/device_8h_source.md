---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/device_8h_source.html
original_path: doxygen/html/device_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

18#include <[zephyr/sys/util.h](util_8h.md)>

19#include <[zephyr/toolchain.h](toolchain_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

32

34

39#define Z\_DEVICE\_DEPS\_SEP INT16\_MIN

40

45#define Z\_DEVICE\_DEPS\_ENDS INT16\_MAX

46

48#define Z\_DEVICE\_IS\_MUTABLE(node\_id) \

49 COND\_CODE\_1(IS\_ENABLED(CONFIG\_DEVICE\_MUTABLE), (DT\_PROP(node\_id, zephyr\_mutable)), (0))

50

52

[ 68](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3);

69

[ 71](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)#define DEVICE\_HANDLE\_NULL 0

72

[ 92](group__device__model.md#ga430eb7530aeb3cff5708b55f9b571eb9)#define DEVICE\_NAME\_GET(dev\_id) \_CONCAT(\_\_device\_, dev\_id)

93

94/\* Node paths can exceed the maximum size supported by

95 \* device\_get\_binding() in user mode; this macro synthesizes a unique

96 \* dev\_id from a devicetree node while staying within this maximum

97 \* size.

98 \*

99 \* The ordinal used in this name can be mapped to the path by

100 \* examining zephyr/include/generated/zephyr/devicetree\_generated.h.

101 \*/

102#define Z\_DEVICE\_DT\_DEV\_ID(node\_id) \_CONCAT(dts\_ord\_, DT\_DEP\_ORD(node\_id))

103

[ 134](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)#define DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, \

135 api) \

136 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

137 Z\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, data, \

138 config, level, prio, api, \

139 &Z\_DEVICE\_STATE\_NAME(dev\_id))

140

[ 152](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)#define DEVICE\_DT\_NAME(node\_id) \

153 DT\_PROP\_OR(node\_id, label, DT\_NODE\_FULL\_NAME(node\_id))

154

[ 162](group__device__model.md#gae16caf17999906091613325f885103cd)#define DEVICE\_DT\_DEFER(node\_id) \

163 DT\_PROP(node\_id, zephyr\_deferred\_init)

164

[ 195](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, \

196 ...) \

197 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

198 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

199 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

200 level, prio, api, \

201 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

202 \_\_VA\_ARGS\_\_)

203

[ 212](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)#define DEVICE\_DT\_INST\_DEFINE(inst, ...) \

213 DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

214

[ 229](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)#define DEVICE\_DT\_NAME\_GET(node\_id) DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

230

[ 246](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)#define DEVICE\_DT\_GET(node\_id) (&DEVICE\_DT\_NAME\_GET(node\_id))

247

[ 257](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)#define DEVICE\_DT\_INST\_GET(inst) DEVICE\_DT\_GET(DT\_DRV\_INST(inst))

258

[ 275](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)#define DEVICE\_DT\_GET\_ANY(compat) \

276 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

277 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

278 (NULL))

279

[ 296](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)#define DEVICE\_DT\_GET\_ONE(compat) \

297 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

298 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

299 (ZERO\_OR\_COMPILE\_ERROR(0)))

300

[ 311](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)#define DEVICE\_DT\_GET\_OR\_NULL(node\_id) \

312 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), \

313 (DEVICE\_DT\_GET(node\_id)), (NULL))

314

[ 325](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)#define DEVICE\_GET(dev\_id) (&DEVICE\_NAME\_GET(dev\_id))

326

[ 341](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)#define DEVICE\_DECLARE(dev\_id) \

342 static const struct device DEVICE\_NAME\_GET(dev\_id)

343

[ 351](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)#define DEVICE\_INIT\_DT\_GET(node\_id) \

352 (&Z\_INIT\_ENTRY\_NAME(DEVICE\_DT\_NAME\_GET(node\_id)))

353

[ 361](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)#define DEVICE\_INIT\_GET(dev\_id) (&Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)))

362

[ 371](structdevice__state.md)struct [device\_state](structdevice__state.md) {

[ 379](structdevice__state.md#a4895f511a9246d27a378253ab82e263e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e);

380

[ 384](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) bool [initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) : 1;

385};

386

387struct [pm\_device\_base](structpm__device__base.md);

388struct [pm\_device](structpm__device.md);

389struct [pm\_device\_isr](structpm__device__isr.md);

390#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

391struct device\_dt\_metadata;

392#endif

393

394#ifdef CONFIG\_DEVICE\_DEPS\_DYNAMIC

395#define Z\_DEVICE\_DEPS\_CONST

396#else

397#define Z\_DEVICE\_DEPS\_CONST const

398#endif

399

[ 403](structdevice.md)struct [device](structdevice.md) {

[ 405](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d) const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d);

[ 407](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc) const void \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

[ 409](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) const void \*[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

[ 411](structdevice.md#abe18f600adc4ab760963928477cc944e) struct [device\_state](structdevice__state.md) \*[state](structdevice.md#abe18f600adc4ab760963928477cc944e);

[ 413](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e) void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

414#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

[ 423](structdevice.md#a1452f3badd041e8eccf726756700e8fe) Z\_DEVICE\_DEPS\_CONST [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

424#endif /\* CONFIG\_DEVICE\_DEPS \*/

425#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

430 union {

[ 431](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99) struct [pm\_device\_base](structpm__device__base.md) \*[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

[ 432](structdevice.md#a204619a873db1b99ea31f1c190760052) struct [pm\_device](structpm__device.md) \*[pm](structdevice.md#a204619a873db1b99ea31f1c190760052);

[ 433](structdevice.md#a1526ad6d863e16287de8f06dff7164dc) struct [pm\_device\_isr](structpm__device__isr.md) \*[pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc);

434 };

435#endif

436#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

[ 437](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba) const struct device\_dt\_metadata \*[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba);

438#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

439};

440

[ 449](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)static inline [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)(const struct [device](structdevice.md) \*dev)

450{

451 [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) ret = [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0);

452 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

453

454 /\* TODO: If/when devices can be constructed that are not part of the

455 \* fixed sequence we'll need another solution.

456 \*/

457 if (dev != NULL) {

458 ret = 1 + ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3))(dev - [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md)));

459 }

460

461 return ret;

462}

463

472static inline const struct [device](structdevice.md) \*

[ 473](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle)

474{

475 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

476 const struct [device](structdevice.md) \*dev = NULL;

477 size\_t numdev;

478

479 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([device](structdevice.md), &numdev);

480

481 if ((dev\_handle > 0) && ((size\_t)dev\_handle <= numdev)) {

482 dev = &[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md))[dev\_handle - 1];

483 }

484

485 return dev;

486}

487

488#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

489

[ 508](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)typedef int (\*[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb))(const struct [device](structdevice.md) \*dev,

509 void \*context);

510

529static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 530](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)(const struct [device](structdevice.md) \*dev, size\_t \*count)

531{

532 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

533

534 if (rv != NULL) {

535 size\_t i = 0;

536

537 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

538 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

539 ++i;

540 }

541 \*count = i;

542 }

543

544 return rv;

545}

546

565static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 566](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)(const struct [device](structdevice.md) \*dev, size\_t \*count)

567{

568 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

569 size\_t region = 0;

570 size\_t i = 0;

571

572 if (rv != NULL) {

573 /\* Fast forward to injected devices \*/

574 while (region != 1) {

575 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

576 region++;

577 }

578 rv++;

579 }

580 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

581 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

582 ++i;

583 }

584 \*count = i;

585 }

586

587 return rv;

588}

589

609static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 610](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)(const struct [device](structdevice.md) \*dev, size\_t \*count)

611{

612 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

613 size\_t region = 0;

614 size\_t i = 0;

615

616 if (rv != NULL) {

617 /\* Fast forward to supporting devices \*/

618 while (region != 2) {

619 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

620 region++;

621 }

622 rv++;

623 }

624 /\* Count supporting devices.

625 \* Trailing NULL's can be injected by gen\_device\_deps.py due to

626 \* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN\_DYNAMIC\_NUM

627 \*/

628 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

629 (rv[i] != [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0))) {

630 ++i;

631 }

632 \*count = i;

633 }

634

635 return rv;

636}

637

[ 668](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)int [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)(const struct [device](structdevice.md) \*dev,

669 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

670 void \*context);

671

[ 701](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)int [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)(const struct [device](structdevice.md) \*dev,

702 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

703 void \*context);

704

705#endif /\* CONFIG\_DEVICE\_DEPS \*/

706

[ 727](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)\_\_syscall const struct [device](structdevice.md) \*[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

728

737size\_t z\_device\_get\_all\_static(const struct [device](structdevice.md) \*\*devices);

738

[ 755](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)\_\_syscall bool [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(const struct [device](structdevice.md) \*dev);

756

[ 771](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)\_\_syscall int [device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)(const struct [device](structdevice.md) \*dev);

772

776

778

783#define Z\_DEVICE\_STATE\_NAME(dev\_id) \_CONCAT(\_\_devstate\_, dev\_id)

784

790#define Z\_DEVICE\_STATE\_DEFINE(dev\_id) \

791 static Z\_DECL\_ALIGN(struct device\_state) Z\_DEVICE\_STATE\_NAME(dev\_id) \

792 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

793

794#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

795

802#define Z\_DEVICE\_DEPS\_NAME(dev\_id) \_CONCAT(\_\_devicedeps\_, dev\_id)

803

809#define Z\_DEVICE\_EXTRA\_DEPS(...) \

810 FOR\_EACH\_NONEMPTY\_TERM(IDENTITY, (,), \_\_VA\_ARGS\_\_)

811

813#define Z\_DEVICE\_DEPS\_SECTION \

814 \_\_attribute\_\_((\_\_section\_\_(".\_\_device\_deps\_pass1")))

815

816#ifdef \_\_cplusplus

817#define Z\_DEVICE\_DEPS\_EXTERN extern

818#else

819#define Z\_DEVICE\_DEPS\_EXTERN

820#endif

821

857#define Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, ...) \

858 extern Z\_DEVICE\_DEPS\_CONST device\_handle\_t Z\_DEVICE\_DEPS\_NAME( \

859 dev\_id)[]; \

860 Z\_DEVICE\_DEPS\_CONST Z\_DECL\_ALIGN(device\_handle\_t) \

861 Z\_DEVICE\_DEPS\_SECTION Z\_DEVICE\_DEPS\_EXTERN \_\_weak \

862 Z\_DEVICE\_DEPS\_NAME(dev\_id)[] = { \

863 COND\_CODE\_1( \

864 DT\_NODE\_EXISTS(node\_id), \

865 (DT\_DEP\_ORD(node\_id), DT\_REQUIRES\_DEP\_ORDS(node\_id)), \

866 (DEVICE\_HANDLE\_NULL,)) /\*\*/ \

867 Z\_DEVICE\_DEPS\_SEP, \

868 Z\_DEVICE\_EXTRA\_DEPS(\_\_VA\_ARGS\_\_) /\*\*/ \

869 Z\_DEVICE\_DEPS\_SEP, \

870 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

871 (DT\_SUPPORTS\_DEP\_ORDS(node\_id)), ()) /\*\*/ \

872 }

873

874#endif /\* CONFIG\_DEVICE\_DEPS \*/

875#if defined(CONFIG\_DEVICE\_DT\_METADATA) || defined(\_\_DOXYGEN\_\_)

879struct device\_dt\_nodelabels {

880 /\* @brief number of elements in the nodelabels array \*/

881 size\_t num\_nodelabels;

882 /\* @brief array of node labels as strings, exactly as they

883 \* appear in the final devicetree

884 \*/

885 const char \*nodelabels[];

886};

887

895struct device\_dt\_metadata {

900 const struct device\_dt\_nodelabels \*nl;

901};

902

921\_\_syscall const struct [device](structdevice.md) \*device\_get\_by\_dt\_nodelabel(const char \*nodelabel);

922

928static inline const struct device\_dt\_nodelabels \*

929device\_get\_dt\_nodelabels(const struct [device](structdevice.md) \*dev)

930{

931 return dev->[dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)->nl;

932}

933

940#define Z\_DEVICE\_MAX\_NODELABEL\_LEN Z\_DEVICE\_MAX\_NAME\_LEN

941

946#define Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_meta\_, dev\_id)

947

952#define Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) UTIL\_CAT(\_\_dev\_dt\_nodelabels\_, dev\_id)

953

960#define Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id) \

961 static const struct device\_dt\_nodelabels \

962 Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id) = { \

963 .num\_nodelabels = DT\_NUM\_NODELABELS(node\_id), \

964 .nodelabels = DT\_NODELABEL\_STRING\_ARRAY(node\_id), \

965 }; \

966 \

967 static const struct device\_dt\_metadata \

968 Z\_DEVICE\_DT\_METADATA\_NAME\_GET(dev\_id) = { \

969 .nl = &Z\_DEVICE\_DT\_NODELABELS\_NAME\_GET(dev\_id), \

970 };

971#endif /\* CONFIG\_DEVICE\_DT\_METADATA \*/

972

980#define Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id) \

981 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

982 (DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)), (0))

983

990#define Z\_DEVICE\_MAX\_NAME\_LEN 48U

991

997#define Z\_DEVICE\_NAME\_CHECK(name) \

998 BUILD\_ASSERT(sizeof(Z\_STRINGIFY(name)) <= Z\_DEVICE\_MAX\_NAME\_LEN, \

999 Z\_STRINGIFY(DEVICE\_NAME\_GET(name)) " too long")

1000

1014#define Z\_DEVICE\_INIT(name\_, pm\_, data\_, config\_, api\_, state\_, deps\_, node\_id\_, \

1015 dev\_id\_) \

1016 { \

1017 .name = name\_, \

1018 .config = (config\_), \

1019 .api = (api\_), \

1020 .state = (state\_), \

1021 .data = (data\_), \

1022 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, (.deps = (deps\_),)) /\*\*/ \

1023 IF\_ENABLED(CONFIG\_PM\_DEVICE, Z\_DEVICE\_INIT\_PM\_BASE(pm\_)) /\*\*/ \

1024 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1025 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id\_), \

1026 (.dt\_meta = &Z\_DEVICE\_DT\_METADATA\_NAME\_GET( \

1027 dev\_id\_),)))) \

1028 }

1029

1030/\*

1031 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1032 \* unions but they require these braces when combined with C99 designated initializers. For

1033 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1034 \*/

1035#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1036# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) ({ .pm\_base = (pm\_),},)

1037#else

1038# define Z\_DEVICE\_INIT\_PM\_BASE(pm\_) (.pm\_base = (pm\_),)

1039#endif

1040

1047#define Z\_DEVICE\_SECTION\_NAME(level, prio) \

1048 \_CONCAT(INIT\_LEVEL\_ORD(level), \_##prio)

1049

1066#define Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, prio, api, state, \

1067 deps) \

1068 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), (), (static)) \

1069 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), (const)) \

1070 STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE( \

1071 device, COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (device\_mutable), (device)), \

1072 Z\_DEVICE\_SECTION\_NAME(level, prio), DEVICE\_NAME\_GET(dev\_id)) = \

1073 Z\_DEVICE\_INIT(name, pm, data, config, api, state, deps, node\_id, dev\_id)

1074

1075/\* deprecated device initialization levels \*/

1076#define Z\_DEVICE\_LEVEL\_DEPRECATED\_EARLY \

1077 \_\_WARN("EARLY device driver level is deprecated")

1078#define Z\_DEVICE\_LEVEL\_DEPRECATED\_PRE\_KERNEL\_1

1079#define Z\_DEVICE\_LEVEL\_DEPRECATED\_PRE\_KERNEL\_2

1080#define Z\_DEVICE\_LEVEL\_DEPRECATED\_POST\_KERNEL

1081#define Z\_DEVICE\_LEVEL\_DEPRECATED\_APPLICATION \

1082 \_\_WARN("APPLICATION device driver level is deprecated")

1083#define Z\_DEVICE\_LEVEL\_DEPRECATED\_SMP \

1084 \_\_WARN("SMP device driver level is deprecated")

1085

1091#define Z\_DEVICE\_LEVEL\_CHECK\_DEPRECATED\_LEVEL(level) \

1092 Z\_DEVICE\_LEVEL\_DEPRECATED\_##level

1093

1104#define Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_, level, prio) \

1105 Z\_DEVICE\_LEVEL\_CHECK\_DEPRECATED\_LEVEL(level) \

1106 \

1107 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan Z\_INIT\_ENTRY\_SECTION( \

1108 level, prio, Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id)) \

1109 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1110 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1111 (init\_fn\_)}, \

1112 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1113 }

1114

1115#define Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_) \

1116 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan \

1117 \_\_attribute\_\_((\_\_section\_\_(".z\_deferred\_init"))) \

1118 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

1119 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

1120 (init\_fn\_)}, \

1121 Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id), \

1122 }

1123

1124/\*

1125 \* Anonymous unions require C11. Some pre-C11 gcc versions have early support for anonymous

1126 \* unions but they require these braces when combined with C99 designated initializers. For

1127 \* more details see https://docs.zephyrproject.org/latest/develop/languages/cpp/

1128 \*/

1129#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

1130# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) { Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) }

1131#else

1132# define Z\_DEVICE\_INIT\_ENTRY\_DEV(node\_id, dev\_id) Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id)

1133#endif

1134

1135#define Z\_DEV\_ENTRY\_DEV(node\_id, dev\_id) \

1136 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = &DEVICE\_NAME\_GET(dev\_id)

1137

1159#define Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, config, \

1160 level, prio, api, state, ...) \

1161 Z\_DEVICE\_NAME\_CHECK(name); \

1162 \

1163 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, \

1164 (Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, \_\_VA\_ARGS\_\_);)) \

1165 \

1166 IF\_ENABLED(CONFIG\_DEVICE\_DT\_METADATA, \

1167 (IF\_ENABLED(DT\_NODE\_EXISTS(node\_id), \

1168 (Z\_DEVICE\_DT\_METADATA\_DEFINE(node\_id, dev\_id);))))\

1169 \

1170 Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, \

1171 prio, api, state, Z\_DEVICE\_DEPS\_NAME(dev\_id)); \

1172 COND\_CODE\_1(DEVICE\_DT\_DEFER(node\_id), \

1173 (Z\_DEFER\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, \

1174 init\_fn)), \

1175 (Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn, \

1176 level, prio)));

1177

1188#define Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL(node\_id) \

1189 extern COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), \

1190 (const)) struct device DEVICE\_DT\_NAME\_GET(node\_id);

1191

1192[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL)

1193

1194

1195

1196#ifdef \_\_cplusplus

1197}

1198#endif

1199

1200#include <zephyr/syscalls/device.h>

1201

1202#endif /\* ZEPHYR\_INCLUDE\_DEVICE\_H\_ \*/

[device\_mmio.h](device__mmio_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)

const struct device \* device\_get\_binding(const char \*name)

Get a device reference from its device::name field.

[device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)

int16\_t device\_handle\_t

Type used to represent a "handle" for a device.

**Definition** device.h:68

[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)

static const device\_handle\_t \* device\_required\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for devicetree dependencies of this device.

**Definition** device.h:530

[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)

static const device\_handle\_t \* device\_supported\_handles\_get(const struct device \*dev, size\_t \*count)

Get the set of handles that this device supports.

**Definition** device.h:610

[device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)

static device\_handle\_t device\_handle\_get(const struct device \*dev)

Get the handle for a given device.

**Definition** device.h:449

[DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)

#define DEVICE\_HANDLE\_NULL

Flag value used to identify an unknown device.

**Definition** device.h:71

[device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)

int device\_required\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly requires.

[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)

static const struct device \* device\_from\_handle(device\_handle\_t dev\_handle)

Get the device corresponding to a handle.

**Definition** device.h:473

[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)

int(\* device\_visitor\_callback\_t)(const struct device \*dev, void \*context)

Prototype for functions used when iterating over a set of devices.

**Definition** device.h:508

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)

static const device\_handle\_t \* device\_injected\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for injected dependencies of this device.

**Definition** device.h:566

[device\_init](group__device__model.md#gaeea4f9c9f14ab12d224378ab90231c09)

int device\_init(const struct device \*dev)

Initialize a device.

[device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)

int device\_supported\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly supports.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2785

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

**Definition** device.h:371

[device\_state::initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad)

bool initialized

Indicates the device initialization function has been invoked.

**Definition** device.h:384

[device\_state::init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e)

uint8\_t init\_res

Device initialization return code (positive errno value).

**Definition** device.h:379

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:431

[device::deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe)

const device\_handle\_t \* deps

Optional pointer to dependencies associated with the device.

**Definition** device.h:423

[device::pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc)

struct pm\_device\_isr \* pm\_isr

**Definition** device.h:433

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:405

[device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052)

struct pm\_device \* pm

**Definition** device.h:432

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:411

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:407

[device::dt\_meta](structdevice.md#adb4f64c583cbc3396d3ffe78fa0169ba)

const struct device\_dt\_metadata \* dt\_meta

**Definition** device.h:437

[pm\_device\_base](structpm__device__base.md)

Device PM info.

**Definition** device.h:139

[pm\_device\_isr](structpm__device__isr.md)

Runtime PM info for device with synchronous PM.

**Definition** device.h:185

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:163

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [device.h](device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
