---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/timeutil_8h_source.html
original_path: doxygen/html/timeutil_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil.h

[Go to the documentation of this file.](timeutil_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \* Copyright (c) 2025 Tenstorrent AI ULC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

21

22#ifndef ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_

23#define ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_

24

25#include <[limits.h](limits_8h.md)>

26#include <[stdbool.h](stdbool_8h.md)>

27#include <stddef.h>

28#include <[stdint.h](stdint_8h.md)>

29#include <time.h>

30

31#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

32#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

33#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

34#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

35#include <[zephyr/sys/util.h](sys_2util_8h.md)>

36#include <[zephyr/toolchain.h](toolchain_8h.md)>

37#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

38

39#ifdef \_\_cplusplus

40extern "C" {

41#endif

42

50

51/\* Base Year value use in calculations in "timeutil\_timegm64" API \*/

[ 52](group__timeutil__repr__apis.md#gaa61359e3ffe7df1994a9265a66834385)#define TIME\_UTILS\_BASE\_YEAR 1900

53

[ 63](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [timeutil\_timegm64](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)(const struct [tm](structtm.md) \*[tm](structtm.md));

64

76[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) timeutil\_timegm(const struct [tm](structtm.md) \*[tm](structtm.md));

77

84

[ 97](structtimeutil__sync__config.md)struct [timeutil\_sync\_config](structtimeutil__sync__config.md) {

[ 105](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ref\_Hz](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7);

106

[ 118](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [local\_Hz](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f);

119};

120

[ 128](structtimeutil__sync__instant.md)struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) {

[ 134](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201);

135

[ 140](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337);

141};

142

[ 153](structtimeutil__sync__state.md)struct [timeutil\_sync\_state](structtimeutil__sync__state.md) {

[ 155](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96) const struct [timeutil\_sync\_config](structtimeutil__sync__config.md) \*[cfg](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96);

156

[ 158](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99) struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) [base](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99);

159

[ 164](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8) struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) [latest](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8);

165

[ 181](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3) float [skew](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3);

182};

183

[ 201](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)int [timeutil\_sync\_state\_update](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)(struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

202 const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*inst);

203

[ 228](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)int [timeutil\_sync\_state\_set\_skew](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)(struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp, float skew,

229 const struct [timeutil\_sync\_instant](structtimeutil__sync__instant.md) \*base);

230

[ 244](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)float [timeutil\_sync\_estimate\_skew](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp);

245

[ 268](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)int [timeutil\_sync\_ref\_from\_local](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

269 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*refp);

270

[ 292](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)int [timeutil\_sync\_local\_from\_ref](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)(const struct [timeutil\_sync\_state](structtimeutil__sync__state.md) \*tsp,

293 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201), [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*localp);

294

[ 313](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [timeutil\_sync\_skew\_to\_ppb](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)(float skew);

314

318

324

[ 337](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)static inline bool [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(const struct [timespec](structtimespec.md) \*ts)

338{

339 \_\_ASSERT\_NO\_MSG(ts != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

340

341 return (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= 0) && (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc));

342}

343

[ 380](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)static inline bool [timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)(struct [timespec](structtimespec.md) \*ts)

381{

382 \_\_ASSERT\_NO\_MSG(ts != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

383

384#if defined(CONFIG\_SPEED\_OPTIMIZATIONS) && HAS\_BUILTIN(\_\_builtin\_add\_overflow)

385

386 int sign = (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= 0) - (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < 0);

387 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sec = (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) \* (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) / (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) +

388 ((ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < 0) && (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) != [LONG\_MIN](limits_8h.md#ae8a44c5a7436466221e0f3859d02420f))) \*

389 [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)((unsigned long)-ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683), (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) +

390 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [LONG\_MIN](limits_8h.md#ae8a44c5a7436466221e0f3859d02420f)) \* (([LONG\_MAX](limits_8h.md#a50fece4db74f09568b2938db583c5655) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) + 1);

391 bool overflow = \_\_builtin\_add\_overflow(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955), sign \* sec, &ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955));

392

393 ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) -= sign \* (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) \* sec;

394

395 if (!overflow) {

396 \_\_ASSERT\_NO\_MSG([timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(ts));

397 }

398

399 return !overflow;

400

401#else

402

403 long sec;

404

405 if (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) {

406 sec = ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) / (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

407 } else if (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < 0) {

408 if ((sizeof(ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)) == sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) && (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [LONG\_MIN](limits_8h.md#ae8a44c5a7436466221e0f3859d02420f))) {

409 sec = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([LONG\_MAX](limits_8h.md#a50fece4db74f09568b2938db583c5655) / [NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5), [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1));

410 } else {

411 sec = [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)((unsigned long)-ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683), [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc));

412 }

413 } else {

414 sec = 0;

415 }

416

417 if ((ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < 0) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < 0) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) - [INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67) < sec)) {

418 /\*

419 \* When `tv\_nsec` is negative and `tv\_sec` is already most negative,

420 \* further subtraction would cause integer overflow.

421 \*/

422 return false;

423 }

424

425 if ((ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) > 0) &&

426 ([INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) - ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < sec)) {

427 /\*

428 \* When `tv\_nsec` is >= `NSEC\_PER\_SEC` and `tv\_sec` is already most

429 \* positive, further addition would cause integer overflow.

430 \*/

431 return false;

432 }

433

434 if (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) >= (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) {

435 ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) += sec;

436 ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) -= sec \* (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

437 } else if (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < 0) {

438 ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) -= sec;

439 ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) += sec \* (long)[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

440 } else {

441 /\* no change: SonarQube was complaining \*/

442 }

443

444 \_\_ASSERT\_NO\_MSG([timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(ts));

445

446 return true;

447

448#endif

449}

450

[ 466](group__timeutil__timespec__apis.md#ga81026756e417d086b4f53306d04c8d10)static inline bool [timespec\_add](group__timeutil__timespec__apis.md#ga81026756e417d086b4f53306d04c8d10)(struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b)

467{

468 \_\_ASSERT\_NO\_MSG((a != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(a));

469 \_\_ASSERT\_NO\_MSG((b != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(b));

470

471#if defined(CONFIG\_SPEED\_OPTIMIZATIONS) && HAS\_BUILTIN(\_\_builtin\_add\_overflow)

472

473 return !\_\_builtin\_add\_overflow(a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955), b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955), &a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) &&

474 !\_\_builtin\_add\_overflow(a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683), b->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683), &a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)) &&

475 [timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)(a);

476

477#else

478

479 if ((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < 0) && (b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < 0) && ([INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67) - a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) > b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955))) {

480 /\* negative integer overflow would occur \*/

481 return false;

482 }

483

484 if ((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) > 0) && (b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) > 0) && ([INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) - a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955))) {

485 /\* positive integer overflow would occur \*/

486 return false;

487 }

488

489 a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) += b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955);

490 a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) += b->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683);

491

492 return [timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)(a);

493

494#endif

495}

496

[ 509](group__timeutil__timespec__apis.md#ga38216267ef6ca24e2b05d77104f5837a)static inline bool [timespec\_negate](group__timeutil__timespec__apis.md#ga38216267ef6ca24e2b05d77104f5837a)(struct [timespec](structtimespec.md) \*ts)

510{

511 \_\_ASSERT\_NO\_MSG((ts != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(ts));

512

513#if defined(CONFIG\_SPEED\_OPTIMIZATIONS) && HAS\_BUILTIN(\_\_builtin\_sub\_overflow)

514

515 return !\_\_builtin\_sub\_overflow(0LL, ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955), &ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) &&

516 !\_\_builtin\_sub\_overflow(0L, ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683), &ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)) && [timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)(ts);

517

518#else

519

520 /\* note: must check for 32-bit size here until #90029 is resolved \*/

521 if (((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe))) ||

522 ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67)))) {

523 /\* -INT64\_MIN > INT64\_MAX, so +ve integer overflow would occur \*/

524 return false;

525 }

526

527 ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) = -ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955);

528 ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) = -ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683);

529

530 return [timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)(ts);

531

532#endif

533}

534

[ 550](group__timeutil__timespec__apis.md#gae0511602aea1fecc0b204e28ae91e7d0)static inline bool [timespec\_sub](group__timeutil__timespec__apis.md#gae0511602aea1fecc0b204e28ae91e7d0)(struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b)

551{

552 \_\_ASSERT\_NO\_MSG(a != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

553 \_\_ASSERT\_NO\_MSG(b != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

554

555 struct [timespec](structtimespec.md) neg = \*b;

556

557 return [timespec\_negate](group__timeutil__timespec__apis.md#ga38216267ef6ca24e2b05d77104f5837a)(&neg) && [timespec\_add](group__timeutil__timespec__apis.md#ga81026756e417d086b4f53306d04c8d10)(a, &neg);

558}

559

[ 572](group__timeutil__timespec__apis.md#gafa281a298f8b2f011875bb00094260fc)static inline int [timespec\_compare](group__timeutil__timespec__apis.md#gafa281a298f8b2f011875bb00094260fc)(const struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b)

573{

574 \_\_ASSERT\_NO\_MSG((a != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(a));

575 \_\_ASSERT\_NO\_MSG((b != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(b));

576

577 return (((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) && (a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) < b->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683))) \* -1) +

578 (((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) && (a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) > b->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683))) \* 1) +

579 ((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) \* -1) + ((a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) > b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)));

580}

581

[ 594](group__timeutil__timespec__apis.md#gaedc15d71f9eee8e243c070a3e07d919f)static inline bool [timespec\_equal](group__timeutil__timespec__apis.md#gaedc15d71f9eee8e243c070a3e07d919f)(const struct [timespec](structtimespec.md) \*a, const struct [timespec](structtimespec.md) \*b)

595{

596 \_\_ASSERT\_NO\_MSG(a != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

597 \_\_ASSERT\_NO\_MSG(b != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

598

599 return (a->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == b->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) && (a->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == b->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683));

600}

601

605

610

[ 620](group__timeutil__repr__apis.md#gab9b5ccdfd7abeaf7a05ebf273cb4d022)static inline void [timespec\_from\_timeout](group__timeutil__repr__apis.md#gab9b5ccdfd7abeaf7a05ebf273cb4d022)([k\_timeout\_t](structk__timeout__t.md) timeout, struct [timespec](structtimespec.md) \*ts)

621{

622 \_\_ASSERT\_NO\_MSG(ts != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

623

624#if defined(CONFIG\_SPEED\_OPTIMIZATIONS)

625

626 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ns = [k\_ticks\_to\_ns\_ceil64](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)(timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa));

627

628 \*ts = (struct [timespec](structtimespec.md)){

629 .[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) = (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) == [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)) \* [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) +

630 (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) != [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)) \* (ns / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)),

631 .tv\_nsec = (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) == [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)) \* ([NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1) +

632 (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) != [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)) \* (ns % [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)),

633 };

634

635#else

636

637 if (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) == 0) {

638 /\* This is equivalent to K\_NO\_WAIT, but without including <zephyr/kernel.h> \*/

639 ts->tv\_sec = 0;

640 ts->tv\_nsec = 0;

641 } else if (timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) == [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)) {

642 /\* This is roughly equivalent to K\_FOREVER, but not including <zephyr/kernel.h> \*/

643 ts->tv\_sec = (time\_t)INT64\_MAX;

644 ts->tv\_nsec = NSEC\_PER\_SEC - 1;

645 } else {

646 uint64\_t ns = k\_ticks\_to\_ns\_ceil64(timeout.ticks);

647

648 ts->tv\_sec = ns / NSEC\_PER\_SEC;

649 ts->tv\_nsec = ns - ts->tv\_sec \* NSEC\_PER\_SEC;

650 }

651

652#endif

653

654 \_\_ASSERT\_NO\_MSG([timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(ts));

655}

656

[ 674](group__timeutil__repr__apis.md#gac4262e7e4ebc2af52d21a18744d50169)static inline [k\_timeout\_t](structk__timeout__t.md) [timespec\_to\_timeout](group__timeutil__repr__apis.md#gac4262e7e4ebc2af52d21a18744d50169)(const struct [timespec](structtimespec.md) \*ts)

675{

676 \_\_ASSERT\_NO\_MSG((ts != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && [timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)(ts));

677

678#if defined(CONFIG\_SPEED\_OPTIMIZATIONS)

679

680 return ([k\_timeout\_t](structk__timeout__t.md)){

681 /\* note: must check for 32-bit size here until #90029 is resolved \*/

682 .ticks = ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) &&

683 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1)) ||

684 ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)) &&

685 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1))) \*

686 [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d) +

687 ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) &&

688 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1)) ||

689 ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) != [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)) &&

690 (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) >= 0))) \*

691 ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_TIMEOUT\_64BIT)

692 ? ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))([CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(

693 [k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) +

694 [k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)(ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)),

695 0, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)))

696 : ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))([CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(

697 [k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) +

698 [k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)(ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)),

699 0, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd))))};

700

701#else

702

703 if ((ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) < 0) || (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == 0 && ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == 0)) {

704 /\* This is equivalent to K\_NO\_WAIT, but without including <zephyr/kernel.h> \*/

705 return ([k\_timeout\_t](structk__timeout__t.md)){

706 .ticks = 0,

707 };

708 /\* note: must check for 32-bit size here until #90029 is resolved \*/

709 } else if (((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) &&

710 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1)) ||

711 ((sizeof(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) == sizeof([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))) && (ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955) == [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)) &&

712 (ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683) == [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) - 1))) {

713 /\* This is equivalent to K\_FOREVER, but not including <zephyr/kernel.h> \*/

714 return ([k\_timeout\_t](structk__timeout__t.md)){

715 .ticks = [K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d),

716 };

717 } else {

718 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_TIMEOUT\_64BIT)) {

719 return ([k\_timeout\_t](structk__timeout__t.md)){

720 .ticks = ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)([k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) +

721 [k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)(ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)),

722 0, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)),

723 };

724 } else {

725 return ([k\_timeout\_t](structk__timeout__t.md)){

726 .ticks = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)([k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)(ts->[tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)) +

727 [k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)(ts->[tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)),

728 0, ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)),

729 };

730 }

731 }

732

733#endif

734}

735

739

740#ifdef \_\_cplusplus

741}

742#endif

743

744#endif /\* ZEPHYR\_INCLUDE\_SYS\_TIMEUTIL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** clock.h:113

[NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)

#define NSEC\_PER\_USEC

number of nanoseconds per microsecond

**Definition** clock.h:83

[K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)

#define K\_TICKS\_FOREVER

**Definition** clock.h:51

[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)

#define USEC\_PER\_SEC

number of microseconds per second

**Definition** clock.h:110

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)

#define CLAMP(val, low, high)

Clamp a value to a given range.

**Definition** util.h:418

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:353

[timespec\_from\_timeout](group__timeutil__repr__apis.md#gab9b5ccdfd7abeaf7a05ebf273cb4d022)

static void timespec\_from\_timeout(k\_timeout\_t timeout, struct timespec \*ts)

Convert a kernel timeout to a timespec.

**Definition** timeutil.h:620

[timespec\_to\_timeout](group__timeutil__repr__apis.md#gac4262e7e4ebc2af52d21a18744d50169)

static k\_timeout\_t timespec\_to\_timeout(const struct timespec \*ts)

Convert a timespec to a kernel timeout.

**Definition** timeutil.h:674

[timeutil\_timegm64](group__timeutil__repr__apis.md#gac4d2957df896a77eb317e10318adf481)

int64\_t timeutil\_timegm64(const struct tm \*tm)

Convert broken-down time to a POSIX epoch offset in seconds.

[timeutil\_sync\_state\_set\_skew](group__timeutil__sync__apis.md#ga01142931b299e848b0642634a0922be5)

int timeutil\_sync\_state\_set\_skew(struct timeutil\_sync\_state \*tsp, float skew, const struct timeutil\_sync\_instant \*base)

Update the state with a new skew and possibly base value.

[timeutil\_sync\_ref\_from\_local](group__timeutil__sync__apis.md#ga75361d2bfd219f1e8107d635eb4ecc16)

int timeutil\_sync\_ref\_from\_local(const struct timeutil\_sync\_state \*tsp, uint64\_t local, uint64\_t \*refp)

Interpolate a reference timescale instant from a local instant.

[timeutil\_sync\_state\_update](group__timeutil__sync__apis.md#gaa6926a23d1c4fbb61584e957d157bd62)

int timeutil\_sync\_state\_update(struct timeutil\_sync\_state \*tsp, const struct timeutil\_sync\_instant \*inst)

Record a new instant in the time synchronization state.

[timeutil\_sync\_skew\_to\_ppb](group__timeutil__sync__apis.md#gabe374cf629ee64b850cc49e954666d8d)

int32\_t timeutil\_sync\_skew\_to\_ppb(float skew)

Convert from a skew to an error in parts-per-billion.

[timeutil\_sync\_estimate\_skew](group__timeutil__sync__apis.md#gac4c25a1ed054a8a06c87d4df9c25ffc6)

float timeutil\_sync\_estimate\_skew(const struct timeutil\_sync\_state \*tsp)

Estimate the skew based on current state.

[timeutil\_sync\_local\_from\_ref](group__timeutil__sync__apis.md#gad8ef92e5dc72bd26d765567134044400)

int timeutil\_sync\_local\_from\_ref(const struct timeutil\_sync\_state \*tsp, uint64\_t ref, int64\_t \*localp)

Interpolate a local timescale instant from a reference instant.

[timespec\_is\_valid](group__timeutil__timespec__apis.md#ga2426889e703021e8b6f8a0ccab885bb6)

static bool timespec\_is\_valid(const struct timespec \*ts)

Check if a timespec is valid.

**Definition** timeutil.h:337

[timespec\_negate](group__timeutil__timespec__apis.md#ga38216267ef6ca24e2b05d77104f5837a)

static bool timespec\_negate(struct timespec \*ts)

Negate a timespec object.

**Definition** timeutil.h:509

[timespec\_normalize](group__timeutil__timespec__apis.md#ga4a0d4891eb6aef6543b1992566729f6c)

static bool timespec\_normalize(struct timespec \*ts)

Normalize a timespec so that the tv\_nsec field is in valid range.

**Definition** timeutil.h:380

[timespec\_add](group__timeutil__timespec__apis.md#ga81026756e417d086b4f53306d04c8d10)

static bool timespec\_add(struct timespec \*a, const struct timespec \*b)

Add one timespec to another.

**Definition** timeutil.h:466

[timespec\_sub](group__timeutil__timespec__apis.md#gae0511602aea1fecc0b204e28ae91e7d0)

static bool timespec\_sub(struct timespec \*a, const struct timespec \*b)

Subtract one timespec from another.

**Definition** timeutil.h:550

[timespec\_equal](group__timeutil__timespec__apis.md#gaedc15d71f9eee8e243c070a3e07d919f)

static bool timespec\_equal(const struct timespec \*a, const struct timespec \*b)

Check if two timespec objects are equal.

**Definition** timeutil.h:594

[timespec\_compare](group__timeutil__timespec__apis.md#gafa281a298f8b2f011875bb00094260fc)

static int timespec\_compare(const struct timespec \*a, const struct timespec \*b)

Compare two timespec objects.

**Definition** timeutil.h:572

[k\_ticks\_to\_ns\_ceil64](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)

#define k\_ticks\_to\_ns\_ceil64(t)

Convert ticks to nanoseconds.

**Definition** time\_units.h:1979

[k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)

#define k\_ns\_to\_ticks\_floor64(t)

Convert nanoseconds to ticks.

**Definition** time\_units.h:1051

[k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)

#define k\_sec\_to\_ticks\_floor64(t)

Convert seconds to ticks.

**Definition** time\_units.h:475

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[limits.h](limits_8h.md)

[LONG\_MAX](limits_8h.md#a50fece4db74f09568b2938db583c5655)

#define LONG\_MAX

**Definition** limits.h:41

[LONG\_MIN](limits_8h.md#ae8a44c5a7436466221e0f3859d02420f)

#define LONG\_MIN

**Definition** limits.h:46

[math\_extras.h](math__extras_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)

#define INT32\_MAX

**Definition** stdint.h:18

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)

#define INT32\_MIN

**Definition** stdint.h:24

[INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67)

#define INT64\_MIN

**Definition** stdint.h:25

[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)

#define UINT32\_MAX

**Definition** stdint.h:29

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071)

#define INT64\_MAX

**Definition** stdint.h:19

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_timeout\_t::ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa)

k\_ticks\_t ticks

**Definition** clock.h:66

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[timespec::tv\_nsec](structtimespec.md#ae3c7510dafa8cbcaede866ed13c99683)

long tv\_nsec

**Definition** \_timespec.h:24

[timespec::tv\_sec](structtimespec.md#afc3302668d7cb5952f590da69fdd4955)

time\_t tv\_sec

**Definition** \_timespec.h:23

[timeutil\_sync\_config](structtimeutil__sync__config.md)

Immutable state for synchronizing two clocks.

**Definition** timeutil.h:97

[timeutil\_sync\_config::ref\_Hz](structtimeutil__sync__config.md#a0ee43492ae85a6305a326046501a8ac7)

uint32\_t ref\_Hz

The nominal instance counter rate in Hz.

**Definition** timeutil.h:105

[timeutil\_sync\_config::local\_Hz](structtimeutil__sync__config.md#a4c180ceb790108292c8c7a825792603f)

uint32\_t local\_Hz

The nominal local counter rate in Hz.

**Definition** timeutil.h:118

[timeutil\_sync\_instant](structtimeutil__sync__instant.md)

Representation of an instant in two time scales.

**Definition** timeutil.h:128

[timeutil\_sync\_instant::ref](structtimeutil__sync__instant.md#a192ad09026e7b511d0961218e34ea201)

uint64\_t ref

An instant in the reference time scale.

**Definition** timeutil.h:134

[timeutil\_sync\_instant::local](structtimeutil__sync__instant.md#a7ebc45287a8ae8d546dc249499f91337)

uint64\_t local

The corresponding instance in the local time scale.

**Definition** timeutil.h:140

[timeutil\_sync\_state](structtimeutil__sync__state.md)

State required to convert instants between time scales.

**Definition** timeutil.h:153

[timeutil\_sync\_state::cfg](structtimeutil__sync__state.md#a2a22936f3ba24fcfb7704e2157ae3e96)

const struct timeutil\_sync\_config \* cfg

Pointer to reference and local rate information.

**Definition** timeutil.h:155

[timeutil\_sync\_state::skew](structtimeutil__sync__state.md#a39454807d207dddb2564d766c8ec2ea3)

float skew

The scale factor used to correct for clock skew.

**Definition** timeutil.h:181

[timeutil\_sync\_state::latest](structtimeutil__sync__state.md#a49dc5405c4818a339a68ad6ef33aa4e8)

struct timeutil\_sync\_instant latest

The most recent instant in both time scales.

**Definition** timeutil.h:164

[timeutil\_sync\_state::base](structtimeutil__sync__state.md#aadbd2ecd98197865e3a71daa8967ce99)

struct timeutil\_sync\_instant base

The base instant in both time scales.

**Definition** timeutil.h:158

[tm](structtm.md)

**Definition** time.h:24

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_clock.h](sys__clock_8h.md)

[time\_units.h](time__units_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [timeutil.h](timeutil_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
