---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/device_8h_source.html
original_path: doxygen/html/device_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

15#include <[zephyr/sys/device\_mmio.h](device__mmio_8h.md)>

16#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

17#include <[zephyr/sys/util.h](util_8h.md)>

18#include <[zephyr/toolchain.h](toolchain_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

29

31

36#define Z\_DEVICE\_DEPS\_SEP INT16\_MIN

37

42#define Z\_DEVICE\_DEPS\_ENDS INT16\_MAX

43

45#define Z\_DEVICE\_IS\_MUTABLE(node\_id) \

46 COND\_CODE\_1(IS\_ENABLED(CONFIG\_DEVICE\_MUTABLE), (DT\_PROP(node\_id, zephyr\_mutable)), (0))

47

49

[ 65](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3);

66

[ 68](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)#define DEVICE\_HANDLE\_NULL 0

69

[ 89](group__device__model.md#ga430eb7530aeb3cff5708b55f9b571eb9)#define DEVICE\_NAME\_GET(dev\_id) \_CONCAT(\_\_device\_, dev\_id)

90

91/\* Node paths can exceed the maximum size supported by

92 \* device\_get\_binding() in user mode; this macro synthesizes a unique

93 \* dev\_id from a devicetree node while staying within this maximum

94 \* size.

95 \*

96 \* The ordinal used in this name can be mapped to the path by

97 \* examining zephyr/include/generated/devicetree\_generated.h.

98 \*/

99#define Z\_DEVICE\_DT\_DEV\_ID(node\_id) \_CONCAT(dts\_ord\_, DT\_DEP\_ORD(node\_id))

100

[ 131](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)#define DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, \

132 api) \

133 Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

134 Z\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, name, init\_fn, pm, data, \

135 config, level, prio, api, \

136 &Z\_DEVICE\_STATE\_NAME(dev\_id))

137

[ 149](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)#define DEVICE\_DT\_NAME(node\_id) \

150 DT\_PROP\_OR(node\_id, label, DT\_NODE\_FULL\_NAME(node\_id))

151

[ 182](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, \

183 ...) \

184 Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

185 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

186 DEVICE\_DT\_NAME(node\_id), init\_fn, pm, data, config, \

187 level, prio, api, \

188 &Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

189 \_\_VA\_ARGS\_\_)

190

[ 199](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)#define DEVICE\_DT\_INST\_DEFINE(inst, ...) \

200 DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

201

[ 216](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)#define DEVICE\_DT\_NAME\_GET(node\_id) DEVICE\_NAME\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

217

[ 233](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)#define DEVICE\_DT\_GET(node\_id) (&DEVICE\_DT\_NAME\_GET(node\_id))

234

[ 244](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)#define DEVICE\_DT\_INST\_GET(inst) DEVICE\_DT\_GET(DT\_DRV\_INST(inst))

245

[ 262](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)#define DEVICE\_DT\_GET\_ANY(compat) \

263 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

264 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

265 (NULL))

266

[ 283](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)#define DEVICE\_DT\_GET\_ONE(compat) \

284 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(compat), \

285 (DEVICE\_DT\_GET(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat))), \

286 (ZERO\_OR\_COMPILE\_ERROR(0)))

287

[ 298](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)#define DEVICE\_DT\_GET\_OR\_NULL(node\_id) \

299 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), \

300 (DEVICE\_DT\_GET(node\_id)), (NULL))

301

[ 312](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)#define DEVICE\_GET(dev\_id) (&DEVICE\_NAME\_GET(dev\_id))

313

[ 328](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)#define DEVICE\_DECLARE(dev\_id) \

329 static const struct device DEVICE\_NAME\_GET(dev\_id)

330

[ 338](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)#define DEVICE\_INIT\_DT\_GET(node\_id) \

339 (&Z\_INIT\_ENTRY\_NAME(DEVICE\_DT\_NAME\_GET(node\_id)))

340

[ 348](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)#define DEVICE\_INIT\_GET(dev\_id) (&Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)))

349

[ 358](structdevice__state.md)struct [device\_state](structdevice__state.md) {

[ 366](structdevice__state.md#a4895f511a9246d27a378253ab82e263e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e);

367

[ 371](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) bool [initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad) : 1;

372};

373

374struct [pm\_device\_base](structpm__device__base.md);

375struct [pm\_device](structpm__device.md);

376struct [pm\_device\_isr](structpm__device__isr.md);

377

378#ifdef CONFIG\_DEVICE\_DEPS\_DYNAMIC

379#define Z\_DEVICE\_DEPS\_CONST

380#else

381#define Z\_DEVICE\_DEPS\_CONST const

382#endif

383

[ 387](structdevice.md)struct [device](structdevice.md) {

[ 389](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d) const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d);

[ 391](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc) const void \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

[ 393](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d) const void \*[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

[ 395](structdevice.md#abe18f600adc4ab760963928477cc944e) struct [device\_state](structdevice__state.md) \*[state](structdevice.md#abe18f600adc4ab760963928477cc944e);

[ 397](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e) void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

398#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

[ 407](structdevice.md#a1452f3badd041e8eccf726756700e8fe) Z\_DEVICE\_DEPS\_CONST [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

408#endif /\* CONFIG\_DEVICE\_DEPS \*/

409#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

414 union {

[ 415](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99) struct [pm\_device\_base](structpm__device__base.md) \*[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

[ 416](structdevice.md#a204619a873db1b99ea31f1c190760052) struct [pm\_device](structpm__device.md) \*[pm](structdevice.md#a204619a873db1b99ea31f1c190760052);

[ 417](structdevice.md#a1526ad6d863e16287de8f06dff7164dc) struct [pm\_device\_isr](structpm__device__isr.md) \*[pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc);

418 };

419#endif

420};

421

[ 430](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)static inline [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)(const struct [device](structdevice.md) \*dev)

431{

432 [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) ret = [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0);

433 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

434

435 /\* TODO: If/when devices can be constructed that are not part of the

436 \* fixed sequence we'll need another solution.

437 \*/

438 if (dev != NULL) {

439 ret = 1 + ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3))(dev - [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md)));

440 }

441

442 return ret;

443}

444

453static inline const struct [device](structdevice.md) \*

[ 454](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle)

455{

456 [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)([device](structdevice.md));

457 const struct [device](structdevice.md) \*dev = NULL;

458 size\_t numdev;

459

460 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([device](structdevice.md), &numdev);

461

462 if ((dev\_handle > 0) && ((size\_t)dev\_handle <= numdev)) {

463 dev = &[STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)([device](structdevice.md))[dev\_handle - 1];

464 }

465

466 return dev;

467}

468

469#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

470

[ 489](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)typedef int (\*[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb))(const struct [device](structdevice.md) \*dev,

490 void \*context);

491

510static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 511](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)(const struct [device](structdevice.md) \*dev, size\_t \*count)

512{

513 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

514

515 if (rv != NULL) {

516 size\_t i = 0;

517

518 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

519 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

520 ++i;

521 }

522 \*count = i;

523 }

524

525 return rv;

526}

527

546static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 547](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)(const struct [device](structdevice.md) \*dev, size\_t \*count)

548{

549 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

550 size\_t region = 0;

551 size\_t i = 0;

552

553 if (rv != NULL) {

554 /\* Fast forward to injected devices \*/

555 while (region != 1) {

556 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

557 region++;

558 }

559 rv++;

560 }

561 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

562 (rv[i] != Z\_DEVICE\_DEPS\_SEP)) {

563 ++i;

564 }

565 \*count = i;

566 }

567

568 return rv;

569}

570

590static inline const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*

[ 591](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)(const struct [device](structdevice.md) \*dev, size\_t \*count)

592{

593 const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \*rv = dev->[deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe);

594 size\_t region = 0;

595 size\_t i = 0;

596

597 if (rv != NULL) {

598 /\* Fast forward to supporting devices \*/

599 while (region != 2) {

600 if (\*rv == Z\_DEVICE\_DEPS\_SEP) {

601 region++;

602 }

603 rv++;

604 }

605 /\* Count supporting devices.

606 \* Trailing NULL's can be injected by gen\_device\_deps.py due to

607 \* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN\_DYNAMIC\_NUM

608 \*/

609 while ((rv[i] != Z\_DEVICE\_DEPS\_ENDS) &&

610 (rv[i] != [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0))) {

611 ++i;

612 }

613 \*count = i;

614 }

615

616 return rv;

617}

618

[ 649](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)int [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)(const struct [device](structdevice.md) \*dev,

650 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

651 void \*context);

652

[ 682](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)int [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)(const struct [device](structdevice.md) \*dev,

683 [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb,

684 void \*context);

685

686#endif /\* CONFIG\_DEVICE\_DEPS \*/

687

[ 708](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)\_\_syscall const struct [device](structdevice.md) \*[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)(const char \*[name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d));

709

718size\_t z\_device\_get\_all\_static(const struct [device](structdevice.md) \*\*devices);

719

734bool z\_device\_is\_ready(const struct [device](structdevice.md) \*dev);

735

[ 752](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)\_\_syscall bool [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(const struct [device](structdevice.md) \*dev);

753

754static inline bool z\_impl\_device\_is\_ready(const struct [device](structdevice.md) \*dev)

755{

756 return z\_device\_is\_ready(dev);

757}

758

762

764

769#define Z\_DEVICE\_STATE\_NAME(dev\_id) \_CONCAT(\_\_devstate\_, dev\_id)

770

776#define Z\_DEVICE\_STATE\_DEFINE(dev\_id) \

777 static Z\_DECL\_ALIGN(struct device\_state) Z\_DEVICE\_STATE\_NAME(dev\_id) \

778 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

779

780#if defined(CONFIG\_DEVICE\_DEPS) || defined(\_\_DOXYGEN\_\_)

781

788#define Z\_DEVICE\_DEPS\_NAME(dev\_id) \_CONCAT(\_\_devicedeps\_, dev\_id)

789

795#define Z\_DEVICE\_EXTRA\_DEPS(...) \

796 FOR\_EACH\_NONEMPTY\_TERM(IDENTITY, (,), \_\_VA\_ARGS\_\_)

797

799#define Z\_DEVICE\_DEPS\_SECTION \

800 \_\_attribute\_\_((\_\_section\_\_(".\_\_device\_deps\_pass1")))

801

802#ifdef \_\_cplusplus

803#define Z\_DEVICE\_DEPS\_EXTERN extern

804#else

805#define Z\_DEVICE\_DEPS\_EXTERN

806#endif

807

843#define Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, ...) \

844 extern Z\_DEVICE\_DEPS\_CONST device\_handle\_t Z\_DEVICE\_DEPS\_NAME( \

845 dev\_id)[]; \

846 Z\_DEVICE\_DEPS\_CONST Z\_DECL\_ALIGN(device\_handle\_t) \

847 Z\_DEVICE\_DEPS\_SECTION Z\_DEVICE\_DEPS\_EXTERN \_\_weak \

848 Z\_DEVICE\_DEPS\_NAME(dev\_id)[] = { \

849 COND\_CODE\_1( \

850 DT\_NODE\_EXISTS(node\_id), \

851 (DT\_DEP\_ORD(node\_id), DT\_REQUIRES\_DEP\_ORDS(node\_id)), \

852 (DEVICE\_HANDLE\_NULL,)) /\*\*/ \

853 Z\_DEVICE\_DEPS\_SEP, \

854 Z\_DEVICE\_EXTRA\_DEPS(\_\_VA\_ARGS\_\_) /\*\*/ \

855 Z\_DEVICE\_DEPS\_SEP, \

856 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

857 (DT\_SUPPORTS\_DEP\_ORDS(node\_id)), ()) /\*\*/ \

858 }

859

860#endif /\* CONFIG\_DEVICE\_DEPS \*/

861

869#define Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id) \

870 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

871 (DT\_DEP\_ORD\_STR\_SORTABLE(node\_id)), (0))

872

879#define Z\_DEVICE\_MAX\_NAME\_LEN 48U

880

886#define Z\_DEVICE\_NAME\_CHECK(name) \

887 BUILD\_ASSERT(sizeof(Z\_STRINGIFY(name)) <= Z\_DEVICE\_MAX\_NAME\_LEN, \

888 Z\_STRINGIFY(DEVICE\_NAME\_GET(name)) " too long")

889

901#define Z\_DEVICE\_INIT(name\_, pm\_, data\_, config\_, api\_, state\_, deps\_) \

902 { \

903 .name = name\_, \

904 .config = (config\_), \

905 .api = (api\_), \

906 .state = (state\_), \

907 .data = (data\_), \

908 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, (.deps = (deps\_),)) /\*\*/ \

909 IF\_ENABLED(CONFIG\_PM\_DEVICE, ({ .pm\_base = (pm\_),)}) /\*\*/ \

910 }

911

918#define Z\_DEVICE\_SECTION\_NAME(level, prio) \

919 \_CONCAT(INIT\_LEVEL\_ORD(level), \_##prio)

920

937#define Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, prio, api, state, \

938 deps) \

939 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), (), (static)) \

940 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), (const)) \

941 STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE( \

942 device, COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (device\_mutable), (device)), \

943 Z\_DEVICE\_SECTION\_NAME(level, prio), DEVICE\_NAME\_GET(dev\_id)) = \

944 Z\_DEVICE\_INIT(name, pm, data, config, api, state, deps)

945

946/\* deprecated device initialization levels \*/

947#define Z\_DEVICE\_LEVEL\_DEPRECATED\_EARLY \

948 \_\_WARN("EARLY device driver level is deprecated")

949#define Z\_DEVICE\_LEVEL\_DEPRECATED\_PRE\_KERNEL\_1

950#define Z\_DEVICE\_LEVEL\_DEPRECATED\_PRE\_KERNEL\_2

951#define Z\_DEVICE\_LEVEL\_DEPRECATED\_POST\_KERNEL

952#define Z\_DEVICE\_LEVEL\_DEPRECATED\_APPLICATION \

953 \_\_WARN("APPLICATION device driver level is deprecated")

954#define Z\_DEVICE\_LEVEL\_DEPRECATED\_SMP \

955 \_\_WARN("SMP device driver level is deprecated")

956

962#define Z\_DEVICE\_LEVEL\_CHECK\_DEPRECATED\_LEVEL(level) \

963 Z\_DEVICE\_LEVEL\_DEPRECATED\_##level

964

975#define Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn\_, level, prio) \

976 Z\_DEVICE\_LEVEL\_CHECK\_DEPRECATED\_LEVEL(level) \

977 \

978 static const Z\_DECL\_ALIGN(struct init\_entry) \_\_used \_\_noasan Z\_INIT\_ENTRY\_SECTION( \

979 level, prio, Z\_DEVICE\_INIT\_SUB\_PRIO(node\_id)) \

980 Z\_INIT\_ENTRY\_NAME(DEVICE\_NAME\_GET(dev\_id)) = { \

981 .init\_fn = {COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

982 (init\_fn\_)}, \

983 { \

984 COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (.dev\_rw), (.dev)) = \

985 &DEVICE\_NAME\_GET(dev\_id), \

986 }, \

987 }

988

1010#define Z\_DEVICE\_DEFINE(node\_id, dev\_id, name, init\_fn, pm, data, config, \

1011 level, prio, api, state, ...) \

1012 Z\_DEVICE\_NAME\_CHECK(name); \

1013 \

1014 IF\_ENABLED(CONFIG\_DEVICE\_DEPS, \

1015 (Z\_DEVICE\_DEPS\_DEFINE(node\_id, dev\_id, \_\_VA\_ARGS\_\_);)) \

1016 \

1017 Z\_DEVICE\_BASE\_DEFINE(node\_id, dev\_id, name, pm, data, config, level, \

1018 prio, api, state, Z\_DEVICE\_DEPS\_NAME(dev\_id)); \

1019 \

1020 Z\_DEVICE\_INIT\_ENTRY\_DEFINE(node\_id, dev\_id, init\_fn, level, prio)

1021

1032#define Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL(node\_id) \

1033 extern COND\_CODE\_1(Z\_DEVICE\_IS\_MUTABLE(node\_id), (), \

1034 (const)) struct device DEVICE\_DT\_NAME\_GET(node\_id);

1035

1036[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_DEVICE\_DECLARE\_INTERNAL)

1037

1038

1039

1040#ifdef \_\_cplusplus

1041}

1042#endif

1043

1044#include <syscalls/device.h>

1045

1046#endif /\* ZEPHYR\_INCLUDE\_DEVICE\_H\_ \*/

[device\_mmio.h](device__mmio_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)

const struct device \* device\_get\_binding(const char \*name)

Get a device reference from its device::name field.

[device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3)

int16\_t device\_handle\_t

Type used to represent a "handle" for a device.

**Definition** device.h:65

[device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618)

static const device\_handle\_t \* device\_required\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for devicetree dependencies of this device.

**Definition** device.h:511

[device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f)

static const device\_handle\_t \* device\_supported\_handles\_get(const struct device \*dev, size\_t \*count)

Get the set of handles that this device supports.

**Definition** device.h:591

[device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203)

static device\_handle\_t device\_handle\_get(const struct device \*dev)

Get the handle for a given device.

**Definition** device.h:430

[DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)

#define DEVICE\_HANDLE\_NULL

Flag value used to identify an unknown device.

**Definition** device.h:68

[device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245)

int device\_required\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly requires.

[device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a)

static const struct device \* device\_from\_handle(device\_handle\_t dev\_handle)

Get the device corresponding to a handle.

**Definition** device.h:454

[device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)

int(\* device\_visitor\_callback\_t)(const struct device \*dev, void \*context)

Prototype for functions used when iterating over a set of devices.

**Definition** device.h:489

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc)

static const device\_handle\_t \* device\_injected\_handles\_get(const struct device \*dev, size\_t \*count)

Get the device handles for injected dependencies of this device.

**Definition** device.h:547

[device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a)

int device\_supported\_foreach(const struct device \*dev, device\_visitor\_callback\_t visitor\_cb, void \*context)

Visit every device that dev directly supports.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2671

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

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:358

[device\_state::initialized](structdevice__state.md#a26bb28bbe4c17c4f0e496d2b04d4a3ad)

bool initialized

Indicates the device initialization function has been invoked.

**Definition** device.h:371

[device\_state::init\_res](structdevice__state.md#a4895f511a9246d27a378253ab82e263e)

uint8\_t init\_res

Device initialization return code (positive errno value).

**Definition** device.h:366

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:415

[device::deps](structdevice.md#a1452f3badd041e8eccf726756700e8fe)

const device\_handle\_t \* deps

Optional pointer to dependencies associated with the device.

**Definition** device.h:407

[device::pm\_isr](structdevice.md#a1526ad6d863e16287de8f06dff7164dc)

struct pm\_device\_isr \* pm\_isr

**Definition** device.h:417

[device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)

const char \* name

Name of the device instance.

**Definition** device.h:389

[device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052)

struct pm\_device \* pm

**Definition** device.h:416

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:395

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[pm\_device\_base](structpm__device__base.md)

Device PM info.

**Definition** device.h:141

[pm\_device\_isr](structpm__device__isr.md)

Runtime PM info for device with synchronous PM.

**Definition** device.h:187

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:165

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [device.h](device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
