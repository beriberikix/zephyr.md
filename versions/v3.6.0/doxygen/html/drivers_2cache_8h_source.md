---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2cache_8h_source.html
original_path: doxygen/html/drivers_2cache_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h

[Go to the documentation of this file.](drivers_2cache_8h.md)

1/\*

2 \* Copyright 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CACHE\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_CACHE\_H\_

14

15#include <stddef.h>

16

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28#if defined(CONFIG\_DCACHE)

29

35void [cache\_data\_enable](group__cache__arch__interface.md#gaec0a2a0374c2c1fe0496f97a5e4a4456)(void);

36

42void [cache\_data\_disable](group__cache__arch__interface.md#gaf8e5056056c5609a8fd878f1b3aeaf5a)(void);

43

53int [cache\_data\_flush\_all](group__cache__arch__interface.md#gae799dfd86b078f74bdeba952aa2eed92)(void);

54

64int [cache\_data\_invd\_all](group__cache__arch__interface.md#gaade1db95fda43b875985d765f0aeee58)(void);

65

75int [cache\_data\_flush\_and\_invd\_all](group__cache__arch__interface.md#gab48cc0cdaf4c6ec64748cb1d4ed51baa)(void);

76

96int [cache\_data\_flush\_range](group__cache__arch__interface.md#gab433cc69a23c0543376615336e80205b)(void \*addr, size\_t size);

97

118int [cache\_data\_invd\_range](group__cache__arch__interface.md#ga91e01cff6a459d21d97cd451ad63a29f)(void \*addr, size\_t size);

119

140int [cache\_data\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga3d5443b3c6f83840c39bc177256ec24f)(void \*addr, size\_t size);

141

142#if defined(CONFIG\_DCACHE\_LINE\_SIZE\_DETECT)

156size\_t [cache\_data\_line\_size\_get](group__cache__arch__interface.md#gafdf1e8c95982a1fe5f39139d0fc6ab25)(void);

157

158#endif /\* CONFIG\_DCACHE\_LINE\_SIZE\_DETECT \*/

159

160#endif /\* CONFIG\_DCACHE \*/

161

162#if defined(CONFIG\_ICACHE)

163

169void [cache\_instr\_enable](group__cache__arch__interface.md#ga5f51912f5dba3e361e5849c4989d8260)(void);

170

176void [cache\_instr\_disable](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)(void);

177

187int [cache\_instr\_flush\_all](group__cache__arch__interface.md#ga3d02e8f383c9b15354c14274bf9daee8)(void);

188

198int [cache\_instr\_invd\_all](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)(void);

199

209int [cache\_instr\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga585fe4e3511d01af2585c439d722e828)(void);

210

230int [cache\_instr\_flush\_range](group__cache__arch__interface.md#ga909eb6d67a146c97ffebd91a08419479)(void \*addr, size\_t size);

231

252int [cache\_instr\_invd\_range](group__cache__arch__interface.md#ga4f334ddb832d247041b95a177a426cb9)(void \*addr, size\_t size);

253

274int [cache\_instr\_flush\_and\_invd\_range](group__cache__arch__interface.md#ga96f1d12e5c52ed4063662cd8853f400c)(void \*addr, size\_t size);

275

276#ifdef CONFIG\_ICACHE\_LINE\_SIZE\_DETECT

290size\_t [cache\_instr\_line\_size\_get](group__cache__arch__interface.md#gaf80d88e95d4eb6ab63301a5dee5a37fe)(void);

291

292#endif /\* CONFIG\_ICACHE\_LINE\_SIZE\_DETECT \*/

293

294#endif /\* CONFIG\_ICACHE \*/

295

296#ifdef \_\_cplusplus

297}

298#endif

299

303

304#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CACHE\_H\_ \*/

[cache\_instr\_invd\_all](group__cache__arch__interface.md#ga1f4241624e3879e8b43556d65867be22)

#define cache\_instr\_invd\_all

**Definition** cache.h:227

[cache\_instr\_disable](group__cache__arch__interface.md#ga287ead9fa07e9c13ba803a1fc3335479)

#define cache\_instr\_disable

**Definition** cache.h:201

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [cache.h](drivers_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
