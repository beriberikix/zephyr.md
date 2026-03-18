---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2pwm_8h_source.html
original_path: doxygen/html/drivers_2pwm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22

23#include <[errno.h](errno_8h.md)>

24#include <[stdint.h](stdint_8h.md)>

25

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/devicetree.h](devicetree_8h.md)>

28#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

29#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

30#include <[zephyr/toolchain.h](toolchain_8h.md)>

31

32#include <[zephyr/dt-bindings/pwm/pwm.h](dt-bindings_2pwm_2pwm_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

43

45/\* Bit 0 is used for PWM\_POLARITY\_NORMAL/PWM\_POLARITY\_INVERTED \*/

46#define PWM\_CAPTURE\_TYPE\_SHIFT 1U

47#define PWM\_CAPTURE\_TYPE\_MASK (3U << PWM\_CAPTURE\_TYPE\_SHIFT)

48#define PWM\_CAPTURE\_MODE\_SHIFT 3U

49#define PWM\_CAPTURE\_MODE\_MASK (1U << PWM\_CAPTURE\_MODE\_SHIFT)

51

[ 53](group__pwm__interface.md#ga5b4b41ccdf8810a77f71c2155a521f44)#define PWM\_CAPTURE\_TYPE\_PERIOD (1U << PWM\_CAPTURE\_TYPE\_SHIFT)

54

[ 56](group__pwm__interface.md#gab883b83cc5418555a437ce128f32ab01)#define PWM\_CAPTURE\_TYPE\_PULSE (2U << PWM\_CAPTURE\_TYPE\_SHIFT)

57

[ 59](group__pwm__interface.md#ga76175b0c2d5187ded5bbd314dc798bd5)#define PWM\_CAPTURE\_TYPE\_BOTH (PWM\_CAPTURE\_TYPE\_PERIOD | \

60 PWM\_CAPTURE\_TYPE\_PULSE)

61

[ 63](group__pwm__interface.md#gad59fe75340facda843cad06993cf1814)#define PWM\_CAPTURE\_MODE\_SINGLE (0U << PWM\_CAPTURE\_MODE\_SHIFT)

64

[ 66](group__pwm__interface.md#gabe9bbff9832b4fa40faa057fad8fdaa9)#define PWM\_CAPTURE\_MODE\_CONTINUOUS (1U << PWM\_CAPTURE\_MODE\_SHIFT)

67

69

78

[ 79](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0);

80

[ 96](structpwm__dt__spec.md)struct [pwm\_dt\_spec](structpwm__dt__spec.md) {

[ 98](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e) const struct [device](structdevice.md) \*[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e);

[ 100](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2);

[ 102](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3);

[ 104](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b) [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b);

105};

106

[ 151](group__pwm__interface.md#ga88b92c580860441c83d1b03db25fc4f1)#define PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name) \

152 { \

153 .dev = DEVICE\_DT\_GET(DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name)), \

154 .channel = DT\_PWMS\_CHANNEL\_BY\_NAME(node\_id, name), \

155 .period = DT\_PWMS\_PERIOD\_BY\_NAME(node\_id, name), \

156 .flags = DT\_PWMS\_FLAGS\_BY\_NAME(node\_id, name), \

157 }

158

[ 171](group__pwm__interface.md#ga104a81a3481362d2da9046c0e93a8cd0)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME(inst, name) \

172 PWM\_DT\_SPEC\_GET\_BY\_NAME(DT\_DRV\_INST(inst), name)

173

[ 192](group__pwm__interface.md#ga5557add2123a7138b64997cd070e0ee6)#define PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(node\_id, name, default\_value) \

193 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, pwms), \

194 (PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name)), \

195 (default\_value))

196

[ 211](group__pwm__interface.md#gac00e53eccaf9eb515aed0921404adb31)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR(inst, name, default\_value) \

212 PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

213

[ 256](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4)#define PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx) \

257 { \

258 .dev = DEVICE\_DT\_GET(DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx)), \

259 .channel = DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx), \

260 .period = DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx), \

261 .flags = DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx), \

262 }

263

[ 275](group__pwm__interface.md#ga3c1c557fa4461e61f4a147fc72f87f8d)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx) \

276 PWM\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

277

[ 295](group__pwm__interface.md#gaf5808fd88b101208681820b53bca33e1)#define PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value) \

296 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, pwms), \

297 (PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)), \

298 (default\_value))

299

[ 313](group__pwm__interface.md#ga7eeef648c3142fced48b7ab52c9c1ead)#define PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value) \

314 PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_DRV\_INST(inst), idx, default\_value)

315

[ 326](group__pwm__interface.md#ga59a79f0b77c5b71252bde126f333a84b)#define PWM\_DT\_SPEC\_GET(node\_id) PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)

327

[ 338](group__pwm__interface.md#gaa346428c6cb1f11aafaa6306486e8a4b)#define PWM\_DT\_SPEC\_INST\_GET(inst) PWM\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

339

[ 352](group__pwm__interface.md#ga82f8efe8f0bc088fdda58c09dd4be4ff)#define PWM\_DT\_SPEC\_GET\_OR(node\_id, default\_value) \

353 PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)

354

[ 367](group__pwm__interface.md#ga6bd84121715beb62a3ca2672dfae0630)#define PWM\_DT\_SPEC\_INST\_GET\_OR(inst, default\_value) \

368 PWM\_DT\_SPEC\_GET\_OR(DT\_DRV\_INST(inst), default\_value)

369

[ 389](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a)typedef void (\*[pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a))(const struct [device](structdevice.md) \*dev,

390 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

391 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles,

392 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles,

393 int status, void \*user\_data);

394

400typedef int (\*pwm\_set\_cycles\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

401 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles,

402 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

403

408typedef int (\*pwm\_get\_cycles\_per\_sec\_t)(const struct [device](structdevice.md) \*dev,

409 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles);

410

411#ifdef CONFIG\_PWM\_CAPTURE

416typedef int (\*pwm\_configure\_capture\_t)(const struct [device](structdevice.md) \*dev,

417 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

418 [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a) cb,

419 void \*user\_data);

420

425typedef int (\*pwm\_enable\_capture\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

426

431typedef int (\*pwm\_disable\_capture\_t)(const struct [device](structdevice.md) \*dev,

432 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

433#endif /\* CONFIG\_PWM\_CAPTURE \*/

434

436\_\_subsystem struct pwm\_driver\_api {

437 pwm\_set\_cycles\_t set\_cycles;

438 pwm\_get\_cycles\_per\_sec\_t get\_cycles\_per\_sec;

439#ifdef CONFIG\_PWM\_CAPTURE

440 pwm\_configure\_capture\_t configure\_capture;

441 pwm\_enable\_capture\_t enable\_capture;

442 pwm\_disable\_capture\_t disable\_capture;

443#endif /\* CONFIG\_PWM\_CAPTURE \*/

444};

446

[ 477](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)\_\_syscall int [pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

478 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse,

479 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

480

481static inline int z\_impl\_pwm\_set\_cycles(const struct [device](structdevice.md) \*dev,

482 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period,

483 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

484{

485 const struct pwm\_driver\_api \*api =

486 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

487

488 if (pulse > period) {

489 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

490 }

491

492 return api->set\_cycles(dev, channel, period, pulse, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

493}

494

[ 506](group__pwm__interface.md#ga310d416087a619f90e946222668135af)\_\_syscall int [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

507 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles);

508

509static inline int z\_impl\_pwm\_get\_cycles\_per\_sec(const struct [device](structdevice.md) \*dev,

510 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

511 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles)

512{

513 const struct pwm\_driver\_api \*api =

514 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

515

516 return api->get\_cycles\_per\_sec(dev, channel, cycles);

517}

518

[ 535](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)static inline int [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

536 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

537{

538 int err;

539 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pulse\_cycles;

540 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) period\_cycles;

541 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

542

543 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

544 if (err < 0) {

545 return err;

546 }

547

548 period\_cycles = (period \* cycles\_per\_sec) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

549 if (period\_cycles > [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) {

550 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

551 }

552

553 pulse\_cycles = (pulse \* cycles\_per\_sec) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

554 if (pulse\_cycles > [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) {

555 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

556 }

557

558 return [pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)(dev, channel, ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))period\_cycles,

559 ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))pulse\_cycles, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

560}

561

[ 581](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9)static inline int [pwm\_set\_dt](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period,

582 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse)

583{

584 return [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e), spec->[channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2), period, pulse, spec->[flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b));

585}

586

[ 602](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)static inline int [pwm\_set\_pulse\_dt](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec,

603 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse)

604{

605 return [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e), spec->[channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2), spec->[period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3), pulse,

606 spec->[flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b));

607}

608

[ 621](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)static inline int [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

622 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*usec)

623{

624 int err;

625 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) temp;

626 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

627

628 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

629 if (err < 0) {

630 return err;

631 }

632

633 if ([u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)(cycles, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1), &temp)) {

634 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

635 }

636

637 \*usec = temp / cycles\_per\_sec;

638

639 return 0;

640}

641

[ 654](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)static inline int [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

655 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*nsec)

656{

657 int err;

658 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) temp;

659 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles\_per\_sec;

660

661 err = [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)(dev, channel, &cycles\_per\_sec);

662 if (err < 0) {

663 return err;

664 }

665

666 if ([u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)(cycles, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc), &temp)) {

667 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

668 }

669

670 \*nsec = temp / cycles\_per\_sec;

671

672 return 0;

673}

674

675#if defined(CONFIG\_PWM\_CAPTURE) || defined(\_\_DOXYGEN\_\_)

[ 704](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)static inline int [pwm\_configure\_capture](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)(const struct [device](structdevice.md) \*dev,

705 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

706 [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a) cb,

707 void \*user\_data)

708{

709 const struct pwm\_driver\_api \*api =

710 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

711

712 if (api->configure\_capture == NULL) {

713 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

714 }

715

716 return api->configure\_capture(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), cb,

717 user\_data);

718}

719#endif /\* CONFIG\_PWM\_CAPTURE \*/

720

[ 739](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)\_\_syscall int [pwm\_enable\_capture](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

740

741#ifdef CONFIG\_PWM\_CAPTURE

742static inline int z\_impl\_pwm\_enable\_capture(const struct [device](structdevice.md) \*dev,

743 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

744{

745 const struct pwm\_driver\_api \*api =

746 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

747

748 if (api->enable\_capture == NULL) {

749 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

750 }

751

752 return api->enable\_capture(dev, channel);

753}

754#endif /\* CONFIG\_PWM\_CAPTURE \*/

755

[ 770](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)\_\_syscall int [pwm\_disable\_capture](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

771

772#ifdef CONFIG\_PWM\_CAPTURE

773static inline int z\_impl\_pwm\_disable\_capture(const struct [device](structdevice.md) \*dev,

774 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel)

775{

776 const struct pwm\_driver\_api \*api =

777 (const struct pwm\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

778

779 if (api->disable\_capture == NULL) {

780 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

781 }

782

783 return api->disable\_capture(dev, channel);

784}

785#endif /\* CONFIG\_PWM\_CAPTURE \*/

786

[ 814](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)\_\_syscall int [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

815 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*period,

816 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout);

817

[ 846](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)static inline int [pwm\_capture\_usec](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

847 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period,

848 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout)

849{

850 int err;

851 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles;

852 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles;

853

854 err = [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), &period\_cycles,

855 &pulse\_cycles, timeout);

856 if (err < 0) {

857 return err;

858 }

859

860 err = [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(dev, channel, period\_cycles, period);

861 if (err < 0) {

862 return err;

863 }

864

865 err = [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)(dev, channel, pulse\_cycles, pulse);

866 if (err < 0) {

867 return err;

868 }

869

870 return 0;

871}

872

[ 901](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)static inline int [pwm\_capture\_nsec](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

902 [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period,

903 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout)

904{

905 int err;

906 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles;

907 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles;

908

909 err = [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743)(dev, channel, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), &period\_cycles,

910 &pulse\_cycles, timeout);

911 if (err < 0) {

912 return err;

913 }

914

915 err = [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(dev, channel, period\_cycles, period);

916 if (err < 0) {

917 return err;

918 }

919

920 err = [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)(dev, channel, pulse\_cycles, pulse);

921 if (err < 0) {

922 return err;

923 }

924

925 return 0;

926}

927

[ 936](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)static inline bool [pwm\_is\_ready\_dt](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)(const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec)

937{

938 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e));

939}

940

941#ifdef \_\_cplusplus

942}

943#endif

944

948

949#include <syscalls/pwm.h>

950

951#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pwm.h](dt-bindings_2pwm_2pwm_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:107

[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)

#define USEC\_PER\_SEC

number of microseconds per second

**Definition** sys\_clock.h:104

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

**Definition** pwm.h:581

[pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a)

void(\* pwm\_capture\_callback\_handler\_t)(const struct device \*dev, uint32\_t channel, uint32\_t period\_cycles, uint32\_t pulse\_cycles, int status, void \*user\_data)

PWM capture callback handler function signature.

**Definition** pwm.h:389

[pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af)

int pwm\_get\_cycles\_per\_sec(const struct device \*dev, uint32\_t channel, uint64\_t \*cycles)

Get the clock rate (cycles per second) for a single PWM output.

[pwm\_capture\_usec](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b)

static int pwm\_capture\_usec(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, uint64\_t \*period, uint64\_t \*pulse, k\_timeout\_t timeout)

Capture a single PWM period/pulse width in microseconds for a single PWM input.

**Definition** pwm.h:846

[pwm\_capture\_nsec](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a)

static int pwm\_capture\_nsec(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, uint64\_t \*period, uint64\_t \*pulse, k\_timeout\_t timeout)

Capture a single PWM period/pulse width in nanoseconds for a single PWM input.

**Definition** pwm.h:901

[pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e)

static int pwm\_cycles\_to\_nsec(const struct device \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*nsec)

Convert from PWM cycles to nanoseconds.

**Definition** pwm.h:654

[pwm\_is\_ready\_dt](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57)

static bool pwm\_is\_ready\_dt(const struct pwm\_dt\_spec \*spec)

Validate that the PWM device is ready.

**Definition** pwm.h:936

[pwm\_set\_pulse\_dt](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da)

static int pwm\_set\_pulse\_dt(const struct pwm\_dt\_spec \*spec, uint32\_t pulse)

Set the period and pulse width in nanoseconds from a struct pwm\_dt\_spec.

**Definition** pwm.h:602

[pwm\_configure\_capture](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb)

static int pwm\_configure\_capture(const struct device \*dev, uint32\_t channel, pwm\_flags\_t flags, pwm\_capture\_callback\_handler\_t cb, void \*user\_data)

Configure PWM period/pulse width capture for a single PWM input.

**Definition** pwm.h:704

[pwm\_enable\_capture](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a)

int pwm\_enable\_capture(const struct device \*dev, uint32\_t channel)

Enable PWM period/pulse width capture for a single PWM input.

[pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01)

static int pwm\_set(const struct device \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, pwm\_flags\_t flags)

Set the period and pulse width in nanoseconds for a single PWM output.

**Definition** pwm.h:535

[pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0)

uint16\_t pwm\_flags\_t

Provides a type to hold PWM configuration flags.

**Definition** pwm.h:79

[pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9)

static int pwm\_cycles\_to\_usec(const struct device \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*usec)

Convert from PWM cycles to microseconds.

**Definition** pwm.h:621

[pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef)

int pwm\_set\_cycles(const struct device \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, pwm\_flags\_t flags)

Set the period and pulse width for a single PWM output.

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:73

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

[math\_extras.h](math__extras_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[pwm\_dt\_spec](structpwm__dt__spec.md)

Container for PWM information specified in devicetree.

**Definition** pwm.h:96

[pwm\_dt\_spec::flags](structpwm__dt__spec.md#a2ddb45cbde80314a5a50dffe2e43921b)

pwm\_flags\_t flags

Flags.

**Definition** pwm.h:104

[pwm\_dt\_spec::channel](structpwm__dt__spec.md#a739a2672afa1d56ec1d865d6d5be47b2)

uint32\_t channel

Channel number.

**Definition** pwm.h:100

[pwm\_dt\_spec::period](structpwm__dt__spec.md#a935c72595e2248ab75ce0c43a394c0b3)

uint32\_t period

Period in nanoseconds.

**Definition** pwm.h:102

[pwm\_dt\_spec::dev](structpwm__dt__spec.md#ad9f2991bcf978940e638d17c5e17311e)

const struct device \* dev

PWM device instance.

**Definition** pwm.h:98

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pwm.h](drivers_2pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
