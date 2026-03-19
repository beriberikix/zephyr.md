---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cache_8h_source.html
original_path: doxygen/html/cache_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h

[Go to the documentation of this file.](cache_8h.md)

1/\*

2 \* Copyright (c) 2015 Wind River Systems, Inc.

3 \* Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_CACHE\_H\_

9#define ZEPHYR\_INCLUDE\_CACHE\_H\_

10

15

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/arch/cpu.h](cpu_8h.md)>

18#include <[zephyr/debug/sparse.h](sparse_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24#if defined(CONFIG\_EXTERNAL\_CACHE)

25#include <[zephyr/drivers/cache.h](drivers_2cache_8h.md)>

26

27#elif defined(CONFIG\_ARCH\_CACHE)

28#include <[zephyr/arch/cache.h](arch_2cache_8h.md)>

29

30#endif

31

37

42

43#define \_CPU DT\_PATH(cpus, cpu\_0)

44

46

[ 53](group__cache__interface.md#ga8e065404f0d13a33f7b04096165b8776)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_cache\_data\_enable](group__cache__interface.md#ga8e065404f0d13a33f7b04096165b8776)(void)

54{

55#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

56 [cache\_data\_enable](group__cache__arch__interface.md#gaec0a2a0374c2c1fe0496f97a5e4a4456)();

57#endif

58}

59

[ 66](group__cache__interface.md#ga7952019e9231e250a37a3226908102ee)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_cache\_data\_disable](group__cache__interface.md#ga7952019e9231e250a37a3226908102ee)(void)

67{

68#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

69 [cache\_data\_disable](group__cache__arch__interface.md#gaf8e5056056c5609a8fd878f1b3aeaf5a)();

70#endif

71}

72

[ 79](group__cache__interface.md#ga98bd00d87195cbf5f99cea4b68765a7f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_cache\_instr\_enable](group__cache__interface.md#ga98bd00d87195cbf5f99cea4b68765a7f)(void)

80{

81#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

82 [cache\_instr\_enable](group__cache__arch__interface.md#ga5f51912f5dba3e361e5849c4989d8260)();

83#endif

84}

85

[ 92](group__cache__interface.md#ga502377e711c5399926992e530456af60)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_cache\_instr\_disable](group__cache__interface.md#ga502377e711c5399926992e530456af60)(void)

93{

94#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

95 [cache\_instr\_disable](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)();

96#endif

97}

98

[ 108](group__cache__interface.md#ga3992ceae117dbd8bd11a5392e8ab2aa3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_data\_flush\_all](group__cache__interface.md#ga3992ceae117dbd8bd11a5392e8ab2aa3)(void)

109{

110#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

111 return [cache\_data\_flush\_all](group__cache__arch__interface.md#gae799dfd86b078f74bdeba952aa2eed92)();

112#endif

113 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

114}

115

[ 125](group__cache__interface.md#ga6846744d9cdfe5d164679f12abe31e48)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_flush\_all](group__cache__interface.md#ga6846744d9cdfe5d164679f12abe31e48)(void)

126{

127#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

128 return [cache\_instr\_flush\_all](group__cache__arch__interface.md#ga3d02e8f383c9b15354c14274bf9daee8)();

129#endif

130 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

131}

132

[ 142](group__cache__interface.md#ga9c7f8f6783196fc226e58d2da1b7781d)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_data\_invd\_all](group__cache__interface.md#ga9c7f8f6783196fc226e58d2da1b7781d)(void)

143{

144#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

145 return [cache\_data\_invd\_all](group__cache__arch__interface.md#gaade1db95fda43b875985d765f0aeee58)();

146#endif

147 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

148}

149

[ 159](group__cache__interface.md#gadc460f782f2642203e1bd4797dd46308)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_invd\_all](group__cache__interface.md#gadc460f782f2642203e1bd4797dd46308)(void)

160{

161#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

162 return [cache\_instr\_invd\_all](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)();

163#endif

164 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

165}

166

[ 176](group__cache__interface.md#gaa38ce02275c001f4c542c6d967be25ac)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_data\_flush\_and\_invd\_all](group__cache__interface.md#gaa38ce02275c001f4c542c6d967be25ac)(void)

177{

178#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

179 return [cache\_data\_flush\_and\_invd\_all](group__cache__arch__interface.md#gab48cc0cdaf4c6ec64748cb1d4ed51baa)();

180#endif

181 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

182}

183

[ 193](group__cache__interface.md#ga3ac77afb61ae32cc0af7bd61e07cf765)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_flush\_and\_invd\_all](group__cache__interface.md#ga3ac77afb61ae32cc0af7bd61e07cf765)(void)

194{

195#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

196 return [cache\_instr\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga585fe4e3511d01af2585c439d722e828)();

197#endif

198 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

199}

200

[ 220](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)\_\_syscall\_always\_inline int [sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)(void \*addr, size\_t size);

221

222static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int z\_impl\_sys\_cache\_data\_flush\_range(void \*addr, size\_t size)

223{

224#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

225 return [cache\_data\_flush\_range](group__cache__arch__interface.md#gab433cc69a23c0543376615336e80205b)(addr, size);

226#endif

227 ARG\_UNUSED(addr);

228 ARG\_UNUSED(size);

229

230 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

231}

232

[ 252](group__cache__interface.md#ga628ee038060351a9958067dfc2e3192c)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_flush\_range](group__cache__interface.md#ga628ee038060351a9958067dfc2e3192c)(void \*addr, size\_t size)

253{

254#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

255 return [cache\_instr\_flush\_range](group__cache__arch__interface.md#ga909eb6d67a146c97ffebd91a08419479)(addr, size);

256#endif

257 ARG\_UNUSED(addr);

258 ARG\_UNUSED(size);

259

260 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

261}

262

[ 283](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e)\_\_syscall\_always\_inline int [sys\_cache\_data\_invd\_range](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e)(void \*addr, size\_t size);

284

285static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int z\_impl\_sys\_cache\_data\_invd\_range(void \*addr, size\_t size)

286{

287#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

288 return [cache\_data\_invd\_range](group__cache__arch__interface.md#ga91e01cff6a459d21d97cd451ad63a29f)(addr, size);

289#endif

290 ARG\_UNUSED(addr);

291 ARG\_UNUSED(size);

292

293 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

294}

295

[ 316](group__cache__interface.md#ga7cc3e53a18492b871b69af8b2d1d0db9)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_invd\_range](group__cache__interface.md#ga7cc3e53a18492b871b69af8b2d1d0db9)(void \*addr, size\_t size)

317{

318#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

319 return [cache\_instr\_invd\_range](group__cache__arch__interface.md#ga4f334ddb832d247041b95a177a426cb9)(addr, size);

320#endif

321 ARG\_UNUSED(addr);

322 ARG\_UNUSED(size);

323

324 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

325}

326

[ 347](group__cache__interface.md#ga51d2bfa0ed0d139d1d299d14e8269eac)\_\_syscall\_always\_inline int [sys\_cache\_data\_flush\_and\_invd\_range](group__cache__interface.md#ga51d2bfa0ed0d139d1d299d14e8269eac)(void \*addr, size\_t size);

348

349static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int z\_impl\_sys\_cache\_data\_flush\_and\_invd\_range(void \*addr, size\_t size)

350{

351#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

352 return [cache\_data\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga3d5443b3c6f83840c39bc177256ec24f)(addr, size);

353#endif

354 ARG\_UNUSED(addr);

355 ARG\_UNUSED(size);

356

357 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

358}

359

[ 380](group__cache__interface.md#ga768ada6618e2b9ddc5ba3bb54ba48773)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_cache\_instr\_flush\_and\_invd\_range](group__cache__interface.md#ga768ada6618e2b9ddc5ba3bb54ba48773)(void \*addr, size\_t size)

381{

382#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_ICACHE)

383 return [cache\_instr\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga96f1d12e5c52ed4063662cd8853f400c)(addr, size);

384#endif

385 ARG\_UNUSED(addr);

386 ARG\_UNUSED(size);

387

388 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

389}

390

[ 407](group__cache__interface.md#ga6b25a6076791c4a559aa20633b49b07e)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) size\_t [sys\_cache\_data\_line\_size\_get](group__cache__interface.md#ga6b25a6076791c4a559aa20633b49b07e)(void)

408{

409#ifdef CONFIG\_DCACHE\_LINE\_SIZE\_DETECT

410 return [cache\_data\_line\_size\_get](group__cache__arch__interface.md#gafdf1e8c95982a1fe5f39139d0fc6ab25)();

411#elif (CONFIG\_DCACHE\_LINE\_SIZE != 0)

412 return CONFIG\_DCACHE\_LINE\_SIZE;

413#else

414 return [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(\_CPU, d\_cache\_line\_size, 0);

415#endif

416}

417

[ 434](group__cache__interface.md#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) size\_t [sys\_cache\_instr\_line\_size\_get](group__cache__interface.md#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1)(void)

435{

436#ifdef CONFIG\_ICACHE\_LINE\_SIZE\_DETECT

437 return [cache\_instr\_line\_size\_get](group__cache__arch__interface.md#gaf80d88e95d4eb6ab63301a5dee5a37fe)();

438#elif (CONFIG\_ICACHE\_LINE\_SIZE != 0)

439 return CONFIG\_ICACHE\_LINE\_SIZE;

440#else

441 return [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(\_CPU, i\_cache\_line\_size, 0);

442#endif

443}

444

[ 458](group__cache__interface.md#ga0d21da511beb423a64d9bb23e6b5dacf)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [sys\_cache\_is\_ptr\_cached](group__cache__interface.md#ga0d21da511beb423a64d9bb23e6b5dacf)(void \*ptr)

459{

460#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_CACHE\_DOUBLEMAP)

461 return [cache\_is\_ptr\_cached](group__cache__arch__interface.md#gab3c3dd74ba3eb870fafe27a82ae6fa69)(ptr);

462#else

463 ARG\_UNUSED(ptr);

464

465 return false;

466#endif

467}

468

[ 482](group__cache__interface.md#gaa02f0bac4addff95dda539dca2b1d4d1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [sys\_cache\_is\_ptr\_uncached](group__cache__interface.md#gaa02f0bac4addff95dda539dca2b1d4d1)(void \*ptr)

483{

484#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_CACHE\_DOUBLEMAP)

485 return [cache\_is\_ptr\_uncached](group__cache__arch__interface.md#ga3444529ef90c2a4de948967fe8cb48b7)(ptr);

486#else

487 ARG\_UNUSED(ptr);

488

489 return false;

490#endif

491}

492

[ 511](group__cache__interface.md#ga773d9fef6f1a2d76927957e73e245ef5)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \_\_sparse\_cache \*[sys\_cache\_cached\_ptr\_get](group__cache__interface.md#ga773d9fef6f1a2d76927957e73e245ef5)(void \*ptr)

512{

513#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_CACHE\_DOUBLEMAP)

514 return [cache\_cached\_ptr](group__cache__arch__interface.md#ga27e186c66d70ec25b665e0e88124a52a)(ptr);

515#else

516 return (\_\_sparse\_force void \_\_sparse\_cache \*)ptr;

517#endif

518}

519

[ 536](group__cache__interface.md#ga1410d43a8c6d16e1b54a32868eaecfe3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \*[sys\_cache\_uncached\_ptr\_get](group__cache__interface.md#ga1410d43a8c6d16e1b54a32868eaecfe3)(void \_\_sparse\_cache \*ptr)

537{

538#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_CACHE\_DOUBLEMAP)

539 return [cache\_uncached\_ptr](group__cache__arch__interface.md#ga11eb33eddf161352f5bbac9a4d6aed90)(ptr);

540#else

541 return (\_\_sparse\_force void \*)ptr;

542#endif

543}

544

545

546#ifdef CONFIG\_LIBMETAL

547static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_cache\_flush(void \*addr, size\_t size)

548{

549 [sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)(addr, size);

550}

551#endif

552

553#include <zephyr/syscalls/cache.h>

554#ifdef \_\_cplusplus

555}

556#endif

557

561

562#endif /\* ZEPHYR\_INCLUDE\_CACHE\_H\_ \*/

[cache.h](arch_2cache_8h.md)

Public APIs for architectural cache controller drivers.

[cpu.h](cpu_8h.md)

[cache.h](drivers_2cache_8h.md)

Public APIs for external cache controller drivers.

[cache\_uncached\_ptr](group__cache__arch__interface.md#ga11eb33eddf161352f5bbac9a4d6aed90)

#define cache\_uncached\_ptr(ptr)

**Definition** cache.h:349

[cache\_instr\_invd\_all](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)

#define cache\_instr\_invd\_all

**Definition** cache.h:227

[cache\_cached\_ptr](group__cache__arch__interface.md#ga27e186c66d70ec25b665e0e88124a52a)

#define cache\_cached\_ptr(ptr)

**Definition** cache.h:346

[cache\_instr\_disable](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)

#define cache\_instr\_disable

**Definition** cache.h:201

[cache\_is\_ptr\_uncached](group__cache__arch__interface.md#ga3444529ef90c2a4de948967fe8cb48b7)

#define cache\_is\_ptr\_uncached(ptr)

**Definition** cache.h:343

[cache\_instr\_flush\_all](group__cache__arch__interface.md#ga3d02e8f383c9b15354c14274bf9daee8)

#define cache\_instr\_flush\_all

**Definition** cache.h:214

[cache\_data\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga3d5443b3c6f83840c39bc177256ec24f)

#define cache\_data\_flush\_and\_invd\_range(addr, size)

**Definition** cache.h:157

[cache\_instr\_invd\_range](group__cache__arch__interface.md#ga4f334ddb832d247041b95a177a426cb9)

#define cache\_instr\_invd\_range(addr, size)

**Definition** cache.h:287

[cache\_instr\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga585fe4e3511d01af2585c439d722e828)

#define cache\_instr\_flush\_and\_invd\_all

**Definition** cache.h:240

[cache\_instr\_enable](group__cache__arch__interface.md#ga5f51912f5dba3e361e5849c4989d8260)

#define cache\_instr\_enable

**Definition** cache.h:192

[cache\_instr\_flush\_range](group__cache__arch__interface.md#ga909eb6d67a146c97ffebd91a08419479)

#define cache\_instr\_flush\_range(addr, size)

**Definition** cache.h:263

[cache\_data\_invd\_range](group__cache__arch__interface.md#ga91e01cff6a459d21d97cd451ad63a29f)

#define cache\_data\_invd\_range(addr, size)

**Definition** cache.h:132

[cache\_instr\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga96f1d12e5c52ed4063662cd8853f400c)

#define cache\_instr\_flush\_and\_invd\_range(addr, size)

**Definition** cache.h:311

[cache\_data\_invd\_all](group__cache__arch__interface.md#gaade1db95fda43b875985d765f0aeee58)

#define cache\_data\_invd\_all

**Definition** cache.h:72

[cache\_is\_ptr\_cached](group__cache__arch__interface.md#gab3c3dd74ba3eb870fafe27a82ae6fa69)

#define cache\_is\_ptr\_cached(ptr)

**Definition** cache.h:340

[cache\_data\_flush\_range](group__cache__arch__interface.md#gab433cc69a23c0543376615336e80205b)

#define cache\_data\_flush\_range(addr, size)

**Definition** cache.h:108

[cache\_data\_flush\_and\_invd\_all](group__cache__arch__interface.md#gab48cc0cdaf4c6ec64748cb1d4ed51baa)

#define cache\_data\_flush\_and\_invd\_all

**Definition** cache.h:85

[cache\_data\_flush\_all](group__cache__arch__interface.md#gae799dfd86b078f74bdeba952aa2eed92)

#define cache\_data\_flush\_all

**Definition** cache.h:59

[cache\_data\_enable](group__cache__arch__interface.md#gaec0a2a0374c2c1fe0496f97a5e4a4456)

#define cache\_data\_enable

**Definition** cache.h:37

[cache\_instr\_line\_size\_get](group__cache__arch__interface.md#gaf80d88e95d4eb6ab63301a5dee5a37fe)

#define cache\_instr\_line\_size\_get

**Definition** cache.h:332

[cache\_data\_disable](group__cache__arch__interface.md#gaf8e5056056c5609a8fd878f1b3aeaf5a)

#define cache\_data\_disable

**Definition** cache.h:46

[cache\_data\_line\_size\_get](group__cache__arch__interface.md#gafdf1e8c95982a1fe5f39139d0fc6ab25)

#define cache\_data\_line\_size\_get

**Definition** cache.h:177

[sys\_cache\_is\_ptr\_cached](group__cache__interface.md#ga0d21da511beb423a64d9bb23e6b5dacf)

static ALWAYS\_INLINE bool sys\_cache\_is\_ptr\_cached(void \*ptr)

Test if a pointer is in cached region.

**Definition** cache.h:458

[sys\_cache\_uncached\_ptr\_get](group__cache__interface.md#ga1410d43a8c6d16e1b54a32868eaecfe3)

static ALWAYS\_INLINE void \* sys\_cache\_uncached\_ptr\_get(void \*ptr)

Return uncached pointer to a RAM address.

**Definition** cache.h:536

[sys\_cache\_data\_flush\_all](group__cache__interface.md#ga3992ceae117dbd8bd11a5392e8ab2aa3)

static ALWAYS\_INLINE int sys\_cache\_data\_flush\_all(void)

Flush the d-cache.

**Definition** cache.h:108

[sys\_cache\_instr\_flush\_and\_invd\_all](group__cache__interface.md#ga3ac77afb61ae32cc0af7bd61e07cf765)

static ALWAYS\_INLINE int sys\_cache\_instr\_flush\_and\_invd\_all(void)

Flush and Invalidate the i-cache.

**Definition** cache.h:193

[sys\_cache\_instr\_line\_size\_get](group__cache__interface.md#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1)

static ALWAYS\_INLINE size\_t sys\_cache\_instr\_line\_size\_get(void)

Get the i-cache line size.

**Definition** cache.h:434

[sys\_cache\_instr\_disable](group__cache__interface.md#ga502377e711c5399926992e530456af60)

static ALWAYS\_INLINE void sys\_cache\_instr\_disable(void)

Disable the i-cache.

**Definition** cache.h:92

[sys\_cache\_data\_flush\_and\_invd\_range](group__cache__interface.md#ga51d2bfa0ed0d139d1d299d14e8269eac)

int sys\_cache\_data\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the d-cache.

[sys\_cache\_data\_invd\_range](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e)

int sys\_cache\_data\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the d-cache.

[sys\_cache\_instr\_flush\_range](group__cache__interface.md#ga628ee038060351a9958067dfc2e3192c)

static ALWAYS\_INLINE int sys\_cache\_instr\_flush\_range(void \*addr, size\_t size)

Flush an address range in the i-cache.

**Definition** cache.h:252

[sys\_cache\_instr\_flush\_all](group__cache__interface.md#ga6846744d9cdfe5d164679f12abe31e48)

static ALWAYS\_INLINE int sys\_cache\_instr\_flush\_all(void)

Flush the i-cache.

**Definition** cache.h:125

[sys\_cache\_data\_line\_size\_get](group__cache__interface.md#ga6b25a6076791c4a559aa20633b49b07e)

static ALWAYS\_INLINE size\_t sys\_cache\_data\_line\_size\_get(void)

Get the d-cache line size.

**Definition** cache.h:407

[sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)

int sys\_cache\_data\_flush\_range(void \*addr, size\_t size)

Flush an address range in the d-cache.

[sys\_cache\_instr\_flush\_and\_invd\_range](group__cache__interface.md#ga768ada6618e2b9ddc5ba3bb54ba48773)

static ALWAYS\_INLINE int sys\_cache\_instr\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the i-cache.

**Definition** cache.h:380

[sys\_cache\_cached\_ptr\_get](group__cache__interface.md#ga773d9fef6f1a2d76927957e73e245ef5)

static ALWAYS\_INLINE void \* sys\_cache\_cached\_ptr\_get(void \*ptr)

Return cached pointer to a RAM address.

**Definition** cache.h:511

[sys\_cache\_data\_disable](group__cache__interface.md#ga7952019e9231e250a37a3226908102ee)

static ALWAYS\_INLINE void sys\_cache\_data\_disable(void)

Disable the d-cache.

**Definition** cache.h:66

[sys\_cache\_instr\_invd\_range](group__cache__interface.md#ga7cc3e53a18492b871b69af8b2d1d0db9)

static ALWAYS\_INLINE int sys\_cache\_instr\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the i-cache.

**Definition** cache.h:316

[sys\_cache\_data\_enable](group__cache__interface.md#ga8e065404f0d13a33f7b04096165b8776)

static ALWAYS\_INLINE void sys\_cache\_data\_enable(void)

Enable the d-cache.

**Definition** cache.h:53

[sys\_cache\_instr\_enable](group__cache__interface.md#ga98bd00d87195cbf5f99cea4b68765a7f)

static ALWAYS\_INLINE void sys\_cache\_instr\_enable(void)

Enable the i-cache.

**Definition** cache.h:79

[sys\_cache\_data\_invd\_all](group__cache__interface.md#ga9c7f8f6783196fc226e58d2da1b7781d)

static ALWAYS\_INLINE int sys\_cache\_data\_invd\_all(void)

Invalidate the d-cache.

**Definition** cache.h:142

[sys\_cache\_is\_ptr\_uncached](group__cache__interface.md#gaa02f0bac4addff95dda539dca2b1d4d1)

static ALWAYS\_INLINE bool sys\_cache\_is\_ptr\_uncached(void \*ptr)

Test if a pointer is in un-cached region.

**Definition** cache.h:482

[sys\_cache\_data\_flush\_and\_invd\_all](group__cache__interface.md#gaa38ce02275c001f4c542c6d967be25ac)

static ALWAYS\_INLINE int sys\_cache\_data\_flush\_and\_invd\_all(void)

Flush and Invalidate the d-cache.

**Definition** cache.h:176

[sys\_cache\_instr\_invd\_all](group__cache__interface.md#gadc460f782f2642203e1bd4797dd46308)

static ALWAYS\_INLINE int sys\_cache\_instr\_invd\_all(void)

Invalidate the i-cache.

**Definition** cache.h:159

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:935

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel.h](kernel_8h.md)

Public kernel APIs.

[sparse.h](sparse_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [cache.h](cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
