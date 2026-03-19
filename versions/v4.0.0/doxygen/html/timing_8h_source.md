---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/timing_8h_source.html
original_path: doxygen/html/timing_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timing.h

[Go to the documentation of this file.](timing_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TIMING\_TIMING\_H\_

8#define ZEPHYR\_INCLUDE\_TIMING\_TIMING\_H\_

9

10#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

11#include <[zephyr/timing/types.h](include_2zephyr_2timing_2types_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

29

40

[ 48](group__timing__api__soc.md#ga46359ee972c8af3540ffd866e1722fd0)void [soc\_timing\_init](group__timing__api__soc.md#ga46359ee972c8af3540ffd866e1722fd0)(void);

49

[ 58](group__timing__api__soc.md#ga38bf58ad86707eba888ebf19b2bb3020)void [soc\_timing\_start](group__timing__api__soc.md#ga38bf58ad86707eba888ebf19b2bb3020)(void);

59

[ 68](group__timing__api__soc.md#ga1d05ea99038456ff1b6b2bf8c5289688)void [soc\_timing\_stop](group__timing__api__soc.md#ga1d05ea99038456ff1b6b2bf8c5289688)(void);

69

[ 84](group__timing__api__soc.md#ga58abe336c243b2edb34d77b8247ac9e2)[timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) [soc\_timing\_counter\_get](group__timing__api__soc.md#ga58abe336c243b2edb34d77b8247ac9e2)(void);

85

[ 100](group__timing__api__soc.md#ga97f010f79b60089b982d60d543e07660)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [soc\_timing\_cycles\_get](group__timing__api__soc.md#ga97f010f79b60089b982d60d543e07660)(volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start,

101 volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end);

102

[ 110](group__timing__api__soc.md#gaf9416f2d3438df707e883e4b4a212a7f)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [soc\_timing\_freq\_get](group__timing__api__soc.md#gaf9416f2d3438df707e883e4b4a212a7f)(void);

111

[ 120](group__timing__api__soc.md#gaa6135848e3b4aa536d977fcbe8b71d5e)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [soc\_timing\_cycles\_to\_ns](group__timing__api__soc.md#gaa6135848e3b4aa536d977fcbe8b71d5e)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles);

121

[ 131](group__timing__api__soc.md#ga54e65aedaaa3befce5ce1f2e92740fdd)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [soc\_timing\_cycles\_to\_ns\_avg](group__timing__api__soc.md#ga54e65aedaaa3befce5ce1f2e92740fdd)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count);

132

[ 140](group__timing__api__soc.md#ga7fecec11527b307c39467745912bd511)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [soc\_timing\_freq\_get\_mhz](group__timing__api__soc.md#ga7fecec11527b307c39467745912bd511)(void);

141

145

156

[ 164](group__timing__api__board.md#ga742db89830e823a804691d1946a8659c)void [board\_timing\_init](group__timing__api__board.md#ga742db89830e823a804691d1946a8659c)(void);

165

[ 174](group__timing__api__board.md#gaf086f6f6881fd1e530a91f56c7ca3972)void [board\_timing\_start](group__timing__api__board.md#gaf086f6f6881fd1e530a91f56c7ca3972)(void);

175

[ 184](group__timing__api__board.md#ga5cf801e99ca32b4dcb86d82c8d4c10d8)void [board\_timing\_stop](group__timing__api__board.md#ga5cf801e99ca32b4dcb86d82c8d4c10d8)(void);

185

[ 200](group__timing__api__board.md#gafda53aa3668e5a98d92d48eec6c6da3a)[timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) [board\_timing\_counter\_get](group__timing__api__board.md#gafda53aa3668e5a98d92d48eec6c6da3a)(void);

201

[ 216](group__timing__api__board.md#ga087f9f0a8915ec2f23e64c2e8b023ec8)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [board\_timing\_cycles\_get](group__timing__api__board.md#ga087f9f0a8915ec2f23e64c2e8b023ec8)(volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start,

217 volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end);

218

[ 226](group__timing__api__board.md#ga905f59f65aae3802906274ff6d8ab1ee)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [board\_timing\_freq\_get](group__timing__api__board.md#ga905f59f65aae3802906274ff6d8ab1ee)(void);

227

[ 236](group__timing__api__board.md#ga05755593eaf5ab7c2cc9af3d33bea343)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [board\_timing\_cycles\_to\_ns](group__timing__api__board.md#ga05755593eaf5ab7c2cc9af3d33bea343)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles);

237

[ 247](group__timing__api__board.md#ga69ec0aee09f8492f293a3e90a49faa83)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [board\_timing\_cycles\_to\_ns\_avg](group__timing__api__board.md#ga69ec0aee09f8492f293a3e90a49faa83)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count);

248

[ 256](group__timing__api__board.md#gac32edf3332275176d6fa7563da0e06ff)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [board\_timing\_freq\_get\_mhz](group__timing__api__board.md#gac32edf3332275176d6fa7563da0e06ff)(void);

257

261

266

267#ifdef CONFIG\_TIMING\_FUNCTIONS

268

[ 274](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47)void [timing\_init](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47)(void);

275

[ 282](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde)void [timing\_start](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde)(void);

283

[ 290](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2)void [timing\_stop](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2)(void);

291

[ 297](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208)static inline [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) [timing\_counter\_get](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208)(void)

298{

299#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

300 return [board\_timing\_counter\_get](group__timing__api__board.md#gafda53aa3668e5a98d92d48eec6c6da3a)();

301#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

302 return [soc\_timing\_counter\_get](group__timing__api__soc.md#ga58abe336c243b2edb34d77b8247ac9e2)();

303#else

304 return [arch\_timing\_counter\_get](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd)();

305#endif

306}

307

[ 318](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timing\_cycles\_get](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955)(volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start,

319 volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end)

320{

321#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

322 return [board\_timing\_cycles\_get](group__timing__api__board.md#ga087f9f0a8915ec2f23e64c2e8b023ec8)(start, end);

323#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

324 return [soc\_timing\_cycles\_get](group__timing__api__soc.md#ga97f010f79b60089b982d60d543e07660)(start, end);

325#else

326 return [arch\_timing\_cycles\_get](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)(start, end);

327#endif

328}

329

[ 335](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timing\_freq\_get](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b)(void)

336{

337#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

338 return [board\_timing\_freq\_get](group__timing__api__board.md#ga905f59f65aae3802906274ff6d8ab1ee)();

339#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

340 return [soc\_timing\_freq\_get](group__timing__api__soc.md#gaf9416f2d3438df707e883e4b4a212a7f)();

341#else

342 return [arch\_timing\_freq\_get](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)();

343#endif

344}

345

[ 352](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timing\_cycles\_to\_ns](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles)

353{

354#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

355 return [board\_timing\_cycles\_to\_ns](group__timing__api__board.md#ga05755593eaf5ab7c2cc9af3d33bea343)(cycles);

356#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

357 return [soc\_timing\_cycles\_to\_ns](group__timing__api__soc.md#gaa6135848e3b4aa536d977fcbe8b71d5e)(cycles);

358#else

359 return [arch\_timing\_cycles\_to\_ns](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe)(cycles);

360#endif

361}

362

[ 370](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timing\_cycles\_to\_ns\_avg](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count)

371{

372#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

373 return [board\_timing\_cycles\_to\_ns\_avg](group__timing__api__board.md#ga69ec0aee09f8492f293a3e90a49faa83)(cycles, count);

374#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

375 return [soc\_timing\_cycles\_to\_ns\_avg](group__timing__api__soc.md#ga54e65aedaaa3befce5ce1f2e92740fdd)(cycles, count);

376#else

377 return [arch\_timing\_cycles\_to\_ns\_avg](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364)(cycles, count);

378#endif

379}

380

[ 386](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timing\_freq\_get\_mhz](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56)(void)

387{

388#if defined(CONFIG\_BOARD\_HAS\_TIMING\_FUNCTIONS)

389 return [board\_timing\_freq\_get\_mhz](group__timing__api__board.md#gac32edf3332275176d6fa7563da0e06ff)();

390#elif defined(CONFIG\_SOC\_HAS\_TIMING\_FUNCTIONS)

391 return [soc\_timing\_freq\_get\_mhz](group__timing__api__soc.md#ga7fecec11527b307c39467745912bd511)();

392#else

393 return [arch\_timing\_freq\_get\_mhz](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)();

394#endif

395}

396

397#endif /\* CONFIG\_TIMING\_FUNCTIONS \*/

398

402

403#ifdef \_\_cplusplus

404}

405#endif

406

407#endif /\* ZEPHYR\_INCLUDE\_TIMING\_TIMING\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[arch\_timing\_freq\_get](group__timing__api__arch.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)

uint64\_t arch\_timing\_freq\_get(void)

Get frequency of counter used (in Hz).

[arch\_timing\_freq\_get\_mhz](group__timing__api__arch.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)

uint32\_t arch\_timing\_freq\_get\_mhz(void)

Get frequency of counter used (in MHz).

[arch\_timing\_cycles\_get](group__timing__api__arch.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)

uint64\_t arch\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)

Get number of cycles between start and end.

[arch\_timing\_cycles\_to\_ns](group__timing__api__arch.md#ga8424bc96c05dcae34b7ffd445e2916fe)

uint64\_t arch\_timing\_cycles\_to\_ns(uint64\_t cycles)

Convert number of cycles into nanoseconds.

[arch\_timing\_cycles\_to\_ns\_avg](group__timing__api__arch.md#ga925b4caff80f1dbac36531b479b24364)

uint64\_t arch\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)

Convert number of cycles into nanoseconds with averaging.

[arch\_timing\_counter\_get](group__timing__api__arch.md#gad7a709477650c8596a96fe080f583fdd)

timing\_t arch\_timing\_counter\_get(void)

Return timing counter.

[board\_timing\_cycles\_to\_ns](group__timing__api__board.md#ga05755593eaf5ab7c2cc9af3d33bea343)

uint64\_t board\_timing\_cycles\_to\_ns(uint64\_t cycles)

Convert number of cycles into nanoseconds.

[board\_timing\_cycles\_get](group__timing__api__board.md#ga087f9f0a8915ec2f23e64c2e8b023ec8)

uint64\_t board\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)

Get number of cycles between start and end.

[board\_timing\_stop](group__timing__api__board.md#ga5cf801e99ca32b4dcb86d82c8d4c10d8)

void board\_timing\_stop(void)

Signal the end of the timing information gathering.

[board\_timing\_cycles\_to\_ns\_avg](group__timing__api__board.md#ga69ec0aee09f8492f293a3e90a49faa83)

uint64\_t board\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)

Convert number of cycles into nanoseconds with averaging.

[board\_timing\_init](group__timing__api__board.md#ga742db89830e823a804691d1946a8659c)

void board\_timing\_init(void)

Initialize the timing subsystem.

[board\_timing\_freq\_get](group__timing__api__board.md#ga905f59f65aae3802906274ff6d8ab1ee)

uint64\_t board\_timing\_freq\_get(void)

Get frequency of counter used (in Hz).

[board\_timing\_freq\_get\_mhz](group__timing__api__board.md#gac32edf3332275176d6fa7563da0e06ff)

uint32\_t board\_timing\_freq\_get\_mhz(void)

Get frequency of counter used (in MHz).

[board\_timing\_start](group__timing__api__board.md#gaf086f6f6881fd1e530a91f56c7ca3972)

void board\_timing\_start(void)

Signal the start of the timing information gathering.

[board\_timing\_counter\_get](group__timing__api__board.md#gafda53aa3668e5a98d92d48eec6c6da3a)

timing\_t board\_timing\_counter\_get(void)

Return timing counter.

[soc\_timing\_stop](group__timing__api__soc.md#ga1d05ea99038456ff1b6b2bf8c5289688)

void soc\_timing\_stop(void)

Signal the end of the timing information gathering.

[soc\_timing\_start](group__timing__api__soc.md#ga38bf58ad86707eba888ebf19b2bb3020)

void soc\_timing\_start(void)

Signal the start of the timing information gathering.

[soc\_timing\_init](group__timing__api__soc.md#ga46359ee972c8af3540ffd866e1722fd0)

void soc\_timing\_init(void)

Initialize the timing subsystem on SoC.

[soc\_timing\_cycles\_to\_ns\_avg](group__timing__api__soc.md#ga54e65aedaaa3befce5ce1f2e92740fdd)

uint64\_t soc\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)

Convert number of cycles into nanoseconds with averaging.

[soc\_timing\_counter\_get](group__timing__api__soc.md#ga58abe336c243b2edb34d77b8247ac9e2)

timing\_t soc\_timing\_counter\_get(void)

Return timing counter.

[soc\_timing\_freq\_get\_mhz](group__timing__api__soc.md#ga7fecec11527b307c39467745912bd511)

uint32\_t soc\_timing\_freq\_get\_mhz(void)

Get frequency of counter used (in MHz).

[soc\_timing\_cycles\_get](group__timing__api__soc.md#ga97f010f79b60089b982d60d543e07660)

uint64\_t soc\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)

Get number of cycles between start and end.

[soc\_timing\_cycles\_to\_ns](group__timing__api__soc.md#gaa6135848e3b4aa536d977fcbe8b71d5e)

uint64\_t soc\_timing\_cycles\_to\_ns(uint64\_t cycles)

Convert number of cycles into nanoseconds.

[soc\_timing\_freq\_get](group__timing__api__soc.md#gaf9416f2d3438df707e883e4b4a212a7f)

uint64\_t soc\_timing\_freq\_get(void)

Get frequency of counter used (in Hz).

[timing\_cycles\_to\_ns](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2)

static uint64\_t timing\_cycles\_to\_ns(uint64\_t cycles)

Convert number of cycles into nanoseconds.

**Definition** timing.h:352

[timing\_cycles\_to\_ns\_avg](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4)

static uint64\_t timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)

Convert number of cycles into nanoseconds with averaging.

**Definition** timing.h:370

[timing\_start](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde)

void timing\_start(void)

Signal the start of the timing information gathering.

[timing\_init](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47)

void timing\_init(void)

Initialize the timing subsystem.

[timing\_freq\_get\_mhz](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56)

static uint32\_t timing\_freq\_get\_mhz(void)

Get frequency of counter used (in MHz).

**Definition** timing.h:386

[timing\_cycles\_get](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955)

static uint64\_t timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)

Get number of cycles between start and end.

**Definition** timing.h:318

[timing\_counter\_get](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208)

static timing\_t timing\_counter\_get(void)

Return timing counter.

**Definition** timing.h:297

[timing\_freq\_get](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b)

static uint64\_t timing\_freq\_get(void)

Get frequency of counter used (in Hz).

**Definition** timing.h:335

[timing\_stop](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2)

void timing\_stop(void)

Signal the end of the timing information gathering.

[types.h](include_2zephyr_2timing_2types_8h.md)

[timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)

uint64\_t timing\_t

**Definition** types.h:10

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [timing](dir_80ed10ac409b2daa43226282975e73af.md)
- [timing.h](timing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
