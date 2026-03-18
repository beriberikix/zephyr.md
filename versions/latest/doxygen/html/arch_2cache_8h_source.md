---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2cache_8h_source.html
original_path: doxygen/html/arch_2cache_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h

[Go to the documentation of this file.](arch_2cache_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_CACHE\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_CACHE\_H\_

14

21

22#if defined(CONFIG\_ARM64)

23#include <[zephyr/arch/arm64/cache.h](arch_2arm64_2cache_8h.md)>

24#elif defined(CONFIG\_XTENSA)

25#include <[zephyr/arch/xtensa/cache.h](arch_2xtensa_2cache_8h.md)>

26#endif

27

28#if defined(CONFIG\_DCACHE) || defined(\_\_DOXYGEN\_\_)

29

[ 35](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)void [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)(void);

36

[ 37](group__cache__arch__interface.md#gaec0a2a0374c2c1fe0496f97a5e4a4456)#define cache\_data\_enable arch\_dcache\_enable

38

[ 44](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)void [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)(void);

45

[ 46](group__cache__arch__interface.md#gaf8e5056056c5609a8fd878f1b3aeaf5a)#define cache\_data\_disable arch\_dcache\_disable

47

[ 57](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)int [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)(void);

58

[ 59](group__cache__arch__interface.md#gae799dfd86b078f74bdeba952aa2eed92)#define cache\_data\_flush\_all arch\_dcache\_flush\_all

60

[ 70](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)int [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)(void);

71

[ 72](group__cache__arch__interface.md#gaade1db95fda43b875985d765f0aeee58)#define cache\_data\_invd\_all arch\_dcache\_invd\_all

73

[ 83](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)int [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)(void);

84

[ 85](group__cache__arch__interface.md#gab48cc0cdaf4c6ec64748cb1d4ed51baa)#define cache\_data\_flush\_and\_invd\_all arch\_dcache\_flush\_and\_invd\_all

86

[ 106](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)int [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)(void \*addr, size\_t size);

107

[ 108](group__cache__arch__interface.md#gab433cc69a23c0543376615336e80205b)#define cache\_data\_flush\_range(addr, size) arch\_dcache\_flush\_range(addr, size)

109

[ 130](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)int [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)(void \*addr, size\_t size);

131

[ 132](group__cache__arch__interface.md#ga91e01cff6a459d21d97cd451ad63a29f)#define cache\_data\_invd\_range(addr, size) arch\_dcache\_invd\_range(addr, size)

133

154

[ 155](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)int [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)(void \*addr, size\_t size);

156

[ 157](group__cache__arch__interface.md#ga3d5443b3c6f83840c39bc177256ec24f)#define cache\_data\_flush\_and\_invd\_range(addr, size) \

158 arch\_dcache\_flush\_and\_invd\_range(addr, size)

159

160#if defined(CONFIG\_DCACHE\_LINE\_SIZE\_DETECT) || defined(\_\_DOXYGEN\_\_)

161

[ 175](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)size\_t [arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)(void);

176

[ 177](group__cache__arch__interface.md#gafdf1e8c95982a1fe5f39139d0fc6ab25)#define cache\_data\_line\_size\_get arch\_dcache\_line\_size\_get

178

179#endif /\* CONFIG\_DCACHE\_LINE\_SIZE\_DETECT || \_\_DOXYGEN\_\_ \*/

180

181#endif /\* CONFIG\_DCACHE || \_\_DOXYGEN\_\_ \*/

182

183#if defined(CONFIG\_ICACHE) || defined(\_\_DOXYGEN\_\_)

184

[ 190](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)void [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)(void);

191

[ 192](group__cache__arch__interface.md#ga5f51912f5dba3e361e5849c4989d8260)#define cache\_instr\_enable arch\_icache\_enable

193

[ 199](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)void [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)(void);

200

[ 201](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)#define cache\_instr\_disable arch\_icache\_disable

202

[ 212](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)int [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)(void);

213

[ 214](group__cache__arch__interface.md#ga3d02e8f383c9b15354c14274bf9daee8)#define cache\_instr\_flush\_all arch\_icache\_flush\_all

215

[ 225](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)int [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)(void);

226

[ 227](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)#define cache\_instr\_invd\_all arch\_icache\_invd\_all

228

[ 238](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)int [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)(void);

239

[ 240](group__cache__arch__interface.md#ga585fe4e3511d01af2585c439d722e828)#define cache\_instr\_flush\_and\_invd\_all arch\_icache\_flush\_and\_invd\_all

241

[ 261](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)int [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)(void \*addr, size\_t size);

262

[ 263](group__cache__arch__interface.md#ga909eb6d67a146c97ffebd91a08419479)#define cache\_instr\_flush\_range(addr, size) arch\_icache\_flush\_range(addr, size)

264

[ 285](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)int [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)(void \*addr, size\_t size);

286

[ 287](group__cache__arch__interface.md#ga4f334ddb832d247041b95a177a426cb9)#define cache\_instr\_invd\_range(addr, size) arch\_icache\_invd\_range(addr, size)

288

[ 309](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)int [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)(void \*addr, size\_t size);

310

[ 311](group__cache__arch__interface.md#ga96f1d12e5c52ed4063662cd8853f400c)#define cache\_instr\_flush\_and\_invd\_range(addr, size) \

312 arch\_icache\_flush\_and\_invd\_range(addr, size)

313

314#if defined(CONFIG\_ICACHE\_LINE\_SIZE\_DETECT) || defined(\_\_DOXYGEN\_\_)

315

329

[ 330](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)size\_t [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)(void);

331

[ 332](group__cache__arch__interface.md#gaf80d88e95d4eb6ab63301a5dee5a37fe)#define cache\_instr\_line\_size\_get arch\_icache\_line\_size\_get

333

334#endif /\* CONFIG\_ICACHE\_LINE\_SIZE\_DETECT || \_\_DOXYGEN\_\_ \*/

335

336#endif /\* CONFIG\_ICACHE || \_\_DOXYGEN\_\_ \*/

337

338#if CONFIG\_CACHE\_DOUBLEMAP || \_\_DOXYGEN\_\_

[ 339](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa)bool [arch\_cache\_is\_ptr\_cached](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa)(void \*ptr);

[ 340](group__cache__arch__interface.md#gab3c3dd74ba3eb870fafe27a82ae6fa69)#define cache\_is\_ptr\_cached(ptr) arch\_cache\_is\_ptr\_cached(ptr)

341

[ 342](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652)bool [arch\_cache\_is\_ptr\_uncached](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652)(void \*ptr);

[ 343](group__cache__arch__interface.md#ga3444529ef90c2a4de948967fe8cb48b7)#define cache\_is\_ptr\_uncached(ptr) arch\_cache\_is\_ptr\_uncached(ptr)

344

[ 345](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c)void \_\_sparse\_cache \*[arch\_cache\_cached\_ptr\_get](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c)(void \*ptr);

[ 346](group__cache__arch__interface.md#ga27e186c66d70ec25b665e0e88124a52a)#define cache\_cached\_ptr(ptr) arch\_cache\_cached\_ptr\_get(ptr)

347

[ 348](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816)void \*[arch\_cache\_uncached\_ptr\_get](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816)(void \_\_sparse\_cache \*ptr);

[ 349](group__cache__arch__interface.md#ga11eb33eddf161352f5bbac9a4d6aed90)#define cache\_uncached\_ptr(ptr) arch\_cache\_uncached\_ptr\_get(ptr)

350#endif /\* CONFIG\_CACHE\_DOUBLEMAP \*/

351

355

356#endif /\* ZEPHYR\_INCLUDE\_ARCH\_CACHE\_H\_ \*/

[cache.h](arch_2arm64_2cache_8h.md)

[cache.h](arch_2xtensa_2cache_8h.md)

[arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)

void arch\_dcache\_disable(void)

Disable the d-cache.

[arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)

void arch\_icache\_disable(void)

Disable the i-cache.

[arch\_cache\_uncached\_ptr\_get](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816)

void \* arch\_cache\_uncached\_ptr\_get(void \*ptr)

[arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)

int arch\_dcache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the d-cache.

[arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)

int arch\_icache\_flush\_and\_invd\_all(void)

Flush and Invalidate the i-cache.

[arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)

int arch\_icache\_flush\_all(void)

Flush the i-cache.

[arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)

int arch\_icache\_invd\_all(void)

Invalidate the i-cache.

[arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)

int arch\_dcache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the d-cache.

[arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)

size\_t arch\_dcache\_line\_size\_get(void)

Get the d-cache line size.

[arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)

size\_t arch\_icache\_line\_size\_get(void)

Get the i-cache line size.

[arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)

int arch\_icache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the i-cache.

[arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)

int arch\_icache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the i-cache.

[arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)

int arch\_dcache\_flush\_all(void)

Flush the d-cache.

[arch\_cache\_is\_ptr\_cached](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa)

bool arch\_cache\_is\_ptr\_cached(void \*ptr)

[arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)

int arch\_icache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the i-cache.

[arch\_cache\_is\_ptr\_uncached](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652)

bool arch\_cache\_is\_ptr\_uncached(void \*ptr)

[arch\_cache\_cached\_ptr\_get](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c)

void \* arch\_cache\_cached\_ptr\_get(void \*ptr)

[arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)

int arch\_dcache\_flush\_and\_invd\_all(void)

Flush and Invalidate the d-cache.

[arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)

int arch\_dcache\_invd\_all(void)

Invalidate the d-cache.

[arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)

void arch\_icache\_enable(void)

Enable the i-cache.

[arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)

int arch\_dcache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the d-cache.

[arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)

void arch\_dcache\_enable(void)

Enable the d-cache.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [cache.h](arch_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
