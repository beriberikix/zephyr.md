---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2pwm_8h_source.html
original_path: doxygen/html/drivers_2pwm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm.h

[Go to the documentation of this file.](drivers_2pwm_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \* Copyright (c) 2020-2021 Vestas Wind Systems A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_H\_

15

24

25#include <[errno.h](errno_8h.md)>

26#include <[stdint.h](stdint_8h.md)>

27

28#include <[zephyr/device.h](device_8h.md)>

29#include <[zephyr/devicetree.h](devicetree_8h.md)>

30#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

31#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

32#include <[zephyr/toolchain.h](toolchain_8h.md)>

33

34#include <[zephyr/dt-bindings/pwm/pwm.h](dt-bindings_2pwm_2pwm_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

45

47/\* Bit 0 is used for PWM\_POLARITY\_NORMAL/PWM\_POLARITY\_INVERTED \*/

48#define PWM\_CAPTURE\_TYPE\_SHIFT 1U

49#define PWM\_CAPTURE\_TYPE\_MASK (3U << PWM\_CAPTURE\_TYPE\_SHIFT)

50#define PWM\_CAPTURE\_MODE\_SHIFT 3U

51#define PWM\_CAPTURE\_MODE\_MASK (1U << PWM\_CAPTURE\_MODE\_SHIFT)

53

[ 55](group__pwm__interface.md#ga5b4b41ccdf8810a77f71c2155a521f44)#define PWM\_CAPTURE\_TYPE\_PERIOD (1U << PWM\_CAPTURE\_TYPE\_SHIFT)

56

[ 58](group__pwm__interface.md#gab883b83cc5418555a437ce128f32ab01)#define PWM\_CAPTURE\_TYPE\_PULSE (2U << PWM\_CAPTURE\_TYPE\_SHIFT)

59

[ 61](group__pwm__interface.md#ga76175b0c2d5187ded5bbd314dc798bd5)#define PWM\_CAPTURE\_TYPE\_BOTH (PWM\_CAPTURE\_TYPE\_PERIOD | \

62 PWM\_CAPTURE\_TYPE\_PULSE)

63

[ 65](group__pwm__interface.md#gad59fe75340facda843cad06993cf1814)#define PWM\_CAPTURE\_MODE\_SINGLE (0U << PWM\_CAPTURE\_MODE\_SHIFT)

66

[ 68](group__pwm__interface.md#gabe9bbff9832b4fa40faa057fad8fdaa9)#define PWM\_CAPTURE\_MODE\_CONTINUOUS (1U << PWM\_CAPTURE\_MODE\_SHIFT)

69

71

80

[ 81](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0);

82

[ 98](structpwm__dt__spec.md)struct [pwm\_dt\_spec](structpwm__dt__spec.md) {

[ 100](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e) const struct [device](structdevice.md) \*[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e);

[ 102](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2);

[ 104](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3);

[ 106](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b) [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b);

107};

108

[ 153](group__pwm__interface.md#ga88b92c580860441c83d1b03db25fc4f1)#define PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name) \

154 { \

155 .dev = DEVICE\_DT\_GET(DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name)), \

156 .channel = DT\_PWMS\_CHANNEL\_BY\_NAME(node\_id, name), \

157 .period = DT\_PWMS\_PERIOD\_BY\_NAME(node\_id, name), \

158 .flags = DT\_PWMS\_FLAGS\_BY\_NAME(node\_id, name), \

159 }

160

[ 173](group__pwm__interface.md#ga104a81a3481362d2da9046c0e93a8cd0)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME(inst, name) \

174 PWM\_DT\_SPEC\_GET\_BY\_NAME(DT\_DRV\_INST(inst), name)

175

[ 194](group__pwm__interface.md#ga5557add2123a7138b64997cd070e0ee6)#define PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(node\_id, name, default\_value) \

195 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, pwms), \

196 (PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name)), \

197 (default\_value))

198

[ 213](group__pwm__interface.md#gac00e53eccaf9eb515aed0921404adb31)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR(inst, name, default\_value) \

214 PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

215

[ 258](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4)#define PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx) \

259 { \

260 .dev = DEVICE\_DT\_GET(DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx)), \

261 .channel = DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx), \

262 .period = DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx), \

263 .flags = DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx), \

264 }

265

[ 277](group__pwm__interface.md#ga3c1c557fa4461e61f4a147fc72f87f8d)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx) \

278 PWM\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

279

[ 297](group__pwm__interface.md#gaf5808fd88b101208681820b53bca33e1)#define PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value) \

298 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, pwms), \

299 (PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)), \

300 (default\_value))

301

[ 315](group__pwm__interface.md#ga7eeef648c3142fced48b7ab52c9c1ead)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value) \

316 PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_DRV\_INST(inst), idx, default\_value)

317

[ 328](group__pwm__interface.md#ga59a79f0b77c5b71252bde126f333a84b)#define PWM\_DT\_SPEC\_GET(node\_id) PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)

329

[ 340](group__pwm__interface.md#gaa346428c6cb1f11aafaa6306486e8a4b)#define PWM\_DT\_SPEC\_INST\_GET(inst) PWM\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

341

[ 354](group__pwm__interface.md#ga82f8efe8f0bc088fdda58c09dd4be4ff)#define PWM\_DT\_SPEC\_GET\_OR(node\_id, default\_value) \

355 PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)

356

[ 369](group__pwm__interface.md#ga6bd84121715beb62a3ca2672dfae0630)#define PWM\_DT\_SPEC\_INST\_GET\_OR(inst, default\_value) \

370 PWM\_DT\_SPEC\_GET\_OR(DT\_DRV\_INST(inst), default\_value)

371

[ 391](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a)typedef void (\*[pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a))(const struct [device](structdevice.md) \*dev,

392 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

393 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles,

394 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles,

395 int status, void \*user\_data);

396

402typedef int (\*pwm\_set\_cycles\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

403 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles,

404 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

405

410typedef int (\*pwm\_get\_cycles\_per\_sec\_t)(const struct [device](structdevice.md) \*dev,

411 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles);

412

413#ifdef CONFIG\_PWM\_CAPTURE

418typedef int (\*pwm\_configure\_capture\_t)(const struct [device](structdevice.md) \*dev,

419 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

420 [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a) cb,

421 void \*user\_data);

422

427typedef int (\*pwm\_enable\_capture\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

428

433typedef int (\*pwm\_disable\_capture\_t)(const struct [device](structdevice.md) \*dev,

434 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

435#endif /\* CONFIG\_PWM\_CAPTURE \*/

436

438\_\_subsystem struct pwm\_driver\_api {

439 pwm\_set\_cycles\_t set\_cycles;

440 pwm\_get\_cycles\_per\_sec\_t get\_cycles\_per\_sec;

441#ifdef CONFIG\_PWM\_CAPTURE

442 pwm\_configure\_capture\_t configure\_capture;

443 pwm\_enable\_capture\_t enable\_capture;

444 pwm\_disable\_capture\_t disable\_capture;

445#endif /\* CONFIG\_PWM\_CAPTURE \*/

446};

448

[ 479](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)\_\_syscall int [pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

480 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse,

481 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

482

483static inline int z\_impl\_pwm\_set\_cycles(const struct [device](structdevice.md) \*dev,

484 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period,

485 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

486{

487 const struct pwm\_driver\_api \*api =

488 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

489

490 if (pulse > period) {

491 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

492 }

493

494 return api->set\_cycles(dev, channel, period, pulse, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

495}

496

[ 508](group__pwm__interface.md#ga310d416087a619f90e946222668135af)\_\_syscall int [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

509 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles);

510

511static inline int z\_impl\_pwm\_get\_cycles\_per\_sec(const struct [device](structdevice.md) \*dev,

512 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

513 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles)

514{

515 const struct pwm\_driver\_api \*api =

516 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

517

518 return api->get\_cycles\_per\_sec(dev, channel, cycles);

519}

520

[ 537](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)static inline int [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

538 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

539{

540 int err;

541 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pulse\_cycles;

542 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) period\_cycles;

543 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

544

545 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

546 if (err < 0) {

547 return err;

548 }

549

550 period\_cycles = (period \* cycles\_per\_sec) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

551 if (period\_cycles > [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) {

552 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

553 }

554

555 pulse\_cycles = (pulse \* cycles\_per\_sec) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

556 if (pulse\_cycles > [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) {

557 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

558 }

559

560 return [pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)(dev, channel, ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))period\_cycles,

561 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))pulse\_cycles, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

562}

563

[ 583](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9)static inline int [pwm\_set\_dt](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period,

584 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse)

585{

586 return [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e), spec->[channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2), period, pulse, spec->[flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b));

587}

588

[ 604](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)static inline int [pwm\_set\_pulse\_dt](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec,

605 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse)

606{

607 return [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e), spec->[channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2), spec->[period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3), pulse,

608 spec->[flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b));

609}

610

[ 623](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)static inline int [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

624 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*usec)

625{

626 int err;

627 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) temp;

628 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

629

630 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

631 if (err < 0) {

632 return err;

633 }

634

635 if ([u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)(cycles, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1), &temp)) {

636 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

637 }

638

639 \*usec = temp / cycles\_per\_sec;

640

641 return 0;

642}

643

[ 656](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)static inline int [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

657 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*nsec)

658{

659 int err;

660 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) temp;

661 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

662

663 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

664 if (err < 0) {

665 return err;

666 }

667

668 if ([u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)(cycles, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc), &temp)) {

669 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

670 }

671

672 \*nsec = temp / cycles\_per\_sec;

673

674 return 0;

675}

676

677#if defined(CONFIG\_PWM\_CAPTURE) || defined(\_\_DOXYGEN\_\_)

[ 706](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)static inline int [pwm\_configure\_capture](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)(const struct [device](structdevice.md) \*dev,

707 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

708 [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a) cb,

709 void \*user\_data)

710{

711 const struct pwm\_driver\_api \*api =

712 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

713

714 if (api->configure\_capture == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

715 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

716 }

717

718 return api->configure\_capture(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), cb,

719 user\_data);

720}

721#endif /\* CONFIG\_PWM\_CAPTURE \*/

722

[ 741](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)\_\_syscall int [pwm\_enable\_capture](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

742

743#ifdef CONFIG\_PWM\_CAPTURE

744static inline int z\_impl\_pwm\_enable\_capture(const struct [device](structdevice.md) \*dev,

745 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

746{

747 const struct pwm\_driver\_api \*api =

748 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

749

750 if (api->enable\_capture == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

751 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

752 }

753

754 return api->enable\_capture(dev, channel);

755}

756#endif /\* CONFIG\_PWM\_CAPTURE \*/

757

[ 772](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)\_\_syscall int [pwm\_disable\_capture](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

773

774#ifdef CONFIG\_PWM\_CAPTURE

775static inline int z\_impl\_pwm\_disable\_capture(const struct [device](structdevice.md) \*dev,

776 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

777{

778 const struct pwm\_driver\_api \*api =

779 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

780

781 if (api->disable\_capture == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

782 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

783 }

784

785 return api->disable\_capture(dev, channel);

786}

787#endif /\* CONFIG\_PWM\_CAPTURE \*/

788

[ 816](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)\_\_syscall int [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

817 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*period,

818 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout);

819

[ 848](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)static inline int [pwm\_capture\_usec](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

849 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period,

850 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout)

851{

852 int err;

853 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles;

854 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles;

855

856 err = [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), &period\_cycles,

857 &pulse\_cycles, timeout);

858 if (err < 0) {

859 return err;

860 }

861

862 err = [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(dev, channel, period\_cycles, period);

863 if (err < 0) {

864 return err;

865 }

866

867 err = [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(dev, channel, pulse\_cycles, pulse);

868 if (err < 0) {

869 return err;

870 }

871

872 return 0;

873}

874

[ 903](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)static inline int [pwm\_capture\_nsec](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

904 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period,

905 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout)

906{

907 int err;

908 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles;

909 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles;

910

911 err = [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), &period\_cycles,

912 &pulse\_cycles, timeout);

913 if (err < 0) {

914 return err;

915 }

916

917 err = [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(dev, channel, period\_cycles, period);

918 if (err < 0) {

919 return err;

920 }

921

922 err = [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(dev, channel, pulse\_cycles, pulse);

923 if (err < 0) {

924 return err;

925 }

926

927 return 0;

928}

929

[ 938](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)static inline bool [pwm\_is\_ready\_dt](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec)

939{

940 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e));

941}

942

943#ifdef \_\_cplusplus

944}

945#endif

946

950

951#include <zephyr/syscalls/pwm.h>

952

953#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pwm.h](dt-bindings_2pwm_2pwm_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:113

[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)

#define USEC\_PER\_SEC

number of microseconds per second

**Definition** sys\_clock.h:110

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)

static bool u64\_mul\_overflow(uint64\_t a, uint64\_t b, uint64\_t \*result)

Multiply two unsigned 64-bit integers.

[pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)

int pwm\_capture\_cycles(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, uint32\_t \*period, uint32\_t \*pulse, k\_timeout\_t timeout)

Capture a single PWM period/pulse width in clock cycles for a single PWM input.

[pwm\_disable\_capture](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)

int pwm\_disable\_capture(const struct device \*dev, uint32\_t channel)

Disable PWM period/pulse width capture for a single PWM input.

[pwm\_set\_dt](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9)

static int pwm\_set\_dt(const struct pwm\_dt\_spec \*spec, uint32\_t period, uint32\_t pulse)

Set the period and pulse width in nanoseconds from a struct pwm\_dt\_spec (with custom period).

**Definition** pwm.h:583

[pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a)

void(\* pwm\_capture\_callback\_handler\_t)(const struct device \*dev, uint32\_t channel, uint32\_t period\_cycles, uint32\_t pulse\_cycles, int status, void \*user\_data)

PWM capture callback handler function signature.

**Definition** pwm.h:391

[pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)

int pwm\_get\_cycles\_per\_sec(const struct device \*dev, uint32\_t channel, uint64\_t \*cycles)

Get the clock rate (cycles per second) for a single PWM output.

[pwm\_capture\_usec](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)

static int pwm\_capture\_usec(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, uint64\_t \*period, uint64\_t \*pulse, k\_timeout\_t timeout)

Capture a single PWM period/pulse width in microseconds for a single PWM input.

**Definition** pwm.h:848

[pwm\_capture\_nsec](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)

static int pwm\_capture\_nsec(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, uint64\_t \*period, uint64\_t \*pulse, k\_timeout\_t timeout)

Capture a single PWM period/pulse width in nanoseconds for a single PWM input.

**Definition** pwm.h:903

[pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)

static int pwm\_cycles\_to\_nsec(const struct device \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*nsec)

Convert from PWM cycles to nanoseconds.

**Definition** pwm.h:656

[pwm\_is\_ready\_dt](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)

static bool pwm\_is\_ready\_dt(const struct pwm\_dt\_spec \*spec)

Validate that the PWM device is ready.

**Definition** pwm.h:938

[pwm\_set\_pulse\_dt](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)

static int pwm\_set\_pulse\_dt(const struct pwm\_dt\_spec \*spec, uint32\_t pulse)

Set the period and pulse width in nanoseconds from a struct pwm\_dt\_spec.

**Definition** pwm.h:604

[pwm\_configure\_capture](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)

static int pwm\_configure\_capture(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, pwm\_capture\_callback\_handler\_t cb, void \*user\_data)

Configure PWM period/pulse width capture for a single PWM input.

**Definition** pwm.h:706

[pwm\_enable\_capture](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)

int pwm\_enable\_capture(const struct device \*dev, uint32\_t channel)

Enable PWM period/pulse width capture for a single PWM input.

[pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)

static int pwm\_set(const struct device \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, pwm\_flags\_t flags)

Set the period and pulse width in nanoseconds for a single PWM output.

**Definition** pwm.h:537

[pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0)

uint16\_t pwm\_flags\_t

Provides a type to hold PWM configuration flags.

**Definition** pwm.h:81

[pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)

static int pwm\_cycles\_to\_usec(const struct device \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*usec)

Convert from PWM cycles to microseconds.

**Definition** pwm.h:623

[pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)

int pwm\_set\_cycles(const struct device \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, pwm\_flags\_t flags)

Set the period and pulse width for a single PWM output.

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:72

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[math\_extras.h](math__extras_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)

#define UINT32\_MAX

**Definition** stdint.h:29

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[pwm\_dt\_spec](structpwm__dt__spec.md)

Container for PWM information specified in devicetree.

**Definition** pwm.h:98

[pwm\_dt\_spec::flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b)

pwm\_flags\_t flags

Flags.

**Definition** pwm.h:106

[pwm\_dt\_spec::channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2)

uint32\_t channel

Channel number.

**Definition** pwm.h:102

[pwm\_dt\_spec::period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3)

uint32\_t period

Period in nanoseconds.

**Definition** pwm.h:104

[pwm\_dt\_spec::dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e)

const struct device \* dev

PWM device instance.

**Definition** pwm.h:100

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pwm.h](drivers_2pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
