---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2xtensa_2cache_8h_source.html
original_path: doxygen/html/arch_2xtensa_2cache_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h

[Go to the documentation of this file.](arch_2xtensa_2cache_8h.md)

1/\*

2 \* Copyright 2021 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_CACHE\_H\_

6#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_CACHE\_H\_

7

8#include <xtensa/config/core-isa.h>

9#include <[zephyr/toolchain.h](toolchain_8h.md)>

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <[zephyr/debug/sparse.h](sparse_8h.md)>

12#include <xtensa/hal.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#define Z\_DCACHE\_MAX (XCHAL\_DCACHE\_SIZE / XCHAL\_DCACHE\_WAYS)

19

20#if XCHAL\_DCACHE\_SIZE

21BUILD\_ASSERT(Z\_IS\_POW2(XCHAL\_DCACHE\_LINESIZE));

22BUILD\_ASSERT(Z\_IS\_POW2(Z\_DCACHE\_MAX));

23#endif

24

25#if defined(CONFIG\_DCACHE) || defined(\_\_DOXYGEN\_\_)

26

[ 28](arch_2xtensa_2cache_8h.md#a67b31dd2c4be8f94d95a7eb9d5f9b3c9)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)(void \*addr, size\_t bytes)

29{

30#if XCHAL\_DCACHE\_SIZE

31 size\_t step = XCHAL\_DCACHE\_LINESIZE;

32 size\_t first = [ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)(addr, step);

33 size\_t last = [ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(((long)addr) + bytes, step);

34 size\_t line;

35

36 for (line = first; bytes && line < last; line += step) {

37 \_\_asm\_\_ volatile("dhwb %0, 0" :: "r"(line));

38 }

39#endif

40 return 0;

41}

42

[ 44](arch_2xtensa_2cache_8h.md#a83106c2dd8004a0d308f26265f20a2c3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)(void \*addr, size\_t bytes)

45{

46#if XCHAL\_DCACHE\_SIZE

47 size\_t step = XCHAL\_DCACHE\_LINESIZE;

48 size\_t first = [ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)(addr, step);

49 size\_t last = [ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(((long)addr) + bytes, step);

50 size\_t line;

51

52 for (line = first; bytes && line < last; line += step) {

53 \_\_asm\_\_ volatile("dhwbi %0, 0" :: "r"(line));

54 }

55#endif

56 return 0;

57}

58

[ 60](arch_2xtensa_2cache_8h.md#a92b35e4648bac37f0ca709054320c125)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)(void \*addr, size\_t bytes)

61{

62#if XCHAL\_DCACHE\_SIZE

63 size\_t step = XCHAL\_DCACHE\_LINESIZE;

64 size\_t first = [ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)(addr, step);

65 size\_t last = [ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(((long)addr) + bytes, step);

66 size\_t line;

67

68 for (line = first; bytes && line < last; line += step) {

69 \_\_asm\_\_ volatile("dhi %0, 0" :: "r"(line));

70 }

71#endif

72 return 0;

73}

74

[ 76](arch_2xtensa_2cache_8h.md#a8a5666d8ab2fd898413d1b836c69adc3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)(void)

77{

78#if XCHAL\_DCACHE\_SIZE

79 size\_t step = XCHAL\_DCACHE\_LINESIZE;

80 size\_t line;

81

82 for (line = 0; line < XCHAL\_DCACHE\_SIZE; line += step) {

83 \_\_asm\_\_ volatile("dii %0, 0" :: "r"(line));

84 }

85#endif

86 return 0;

87}

88

[ 90](arch_2xtensa_2cache_8h.md#a3386effa850b7b46773a7ca082d2f695)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)(void)

91{

92#if XCHAL\_DCACHE\_SIZE

93 size\_t step = XCHAL\_DCACHE\_LINESIZE;

94 size\_t line;

95

96 for (line = 0; line < XCHAL\_DCACHE\_SIZE; line += step) {

97 \_\_asm\_\_ volatile("diwb %0, 0" :: "r"(line));

98 }

99#endif

100 return 0;

101}

102

[ 104](arch_2xtensa_2cache_8h.md#a61de91dc463ddc8f53855bbb68776752)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)(void)

105{

106#if XCHAL\_DCACHE\_SIZE

107 size\_t step = XCHAL\_DCACHE\_LINESIZE;

108 size\_t line;

109

110 for (line = 0; line < XCHAL\_DCACHE\_SIZE; line += step) {

111 \_\_asm\_\_ volatile("diwbi %0, 0" :: "r"(line));

112 }

113#endif

114 return 0;

115}

116

[ 118](arch_2xtensa_2cache_8h.md#a2d311a83cbd78a7d959cc0216d42701b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)(void)

119{

120 /\* nothing \*/

121}

122

[ 124](arch_2xtensa_2cache_8h.md#af789498070dadadafd15af00900fae8b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)(void)

125{

126 /\* nothing \*/

127}

128

129#endif /\* CONFIG\_DCACHE \*/

130

131#if defined(CONFIG\_ICACHE) || defined(\_\_DOXYGEN\_\_)

132

[ 134](arch_2xtensa_2cache_8h.md#aafeb5923d0e811759cee20e5f7dcb40a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) size\_t [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)(void)

135{

136 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

137}

138

[ 140](arch_2xtensa_2cache_8h.md#ae6cb0ef4fbcbffc551daf428bffbb54b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)(void)

141{

142 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

143}

144

[ 146](arch_2xtensa_2cache_8h.md#afbd63018906d9d721eb752340bc111d9)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)(void)

147{

148#if XCHAL\_ICACHE\_SIZE

149 xthal\_icache\_all\_invalidate();

150#endif

151 return 0;

152}

153

[ 155](arch_2xtensa_2cache_8h.md#a51cab7fde80d6c07621ac721f73d8e1c)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)(void)

156{

157 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

158}

159

[ 161](arch_2xtensa_2cache_8h.md#aa676959f8b53e0860be8a92b2ae0e56f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)(void \*addr, size\_t size)

162{

163 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

164}

165

[ 167](arch_2xtensa_2cache_8h.md#ad1fcc25b06988a18ae2d3ba28d26faea)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)(void \*addr, size\_t size)

168{

169#if XCHAL\_ICACHE\_SIZE

170 xthal\_icache\_region\_invalidate(addr, size);

171#endif

172 return 0;

173}

174

[ 176](arch_2xtensa_2cache_8h.md#a731ad4f69a6d52df276d09a662ea5f0a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)(void \*addr, size\_t size)

177{

178 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

179}

180

[ 182](arch_2xtensa_2cache_8h.md#a4420e7af2ca86b8da4b3d720d61cbf3b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)(void)

183{

184 /\* nothing \*/

185}

186

[ 188](arch_2xtensa_2cache_8h.md#a3529c39dad808265db75036938ea8a61)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)(void)

189{

190 /\* nothing \*/

191}

192

193#endif /\* CONFIG\_ICACHE \*/

194

195#if defined(CONFIG\_CACHE\_DOUBLEMAP)

209static inline bool [arch\_cache\_is\_ptr\_cached](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa)(void \*ptr)

210{

211 size\_t addr = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) ptr;

212

213 return (addr >> 29) == CONFIG\_XTENSA\_CACHED\_REGION;

214}

215

229static inline bool [arch\_cache\_is\_ptr\_uncached](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652)(void \*ptr)

230{

231 size\_t addr = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) ptr;

232

233 return (addr >> 29) == CONFIG\_XTENSA\_UNCACHED\_REGION;

234}

235

236static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_xtrpoflip([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rto, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rfrom)

237{

238 /\* The math here is all compile-time: when the two regions

239 \* differ by a power of two, we can convert between them by

240 \* setting or clearing just one bit. Otherwise it needs two

241 \* operations.

242 \*/

243 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rxor = (rto ^ rfrom) << 29;

244

245 rto <<= 29;

246 if (Z\_IS\_POW2(rxor)) {

247 if ((rxor & rto) == 0) {

248 return addr & ~rxor;

249 } else {

250 return addr | rxor;

251 }

252 } else {

253 return (addr & ~(7U << 29)) | rto;

254 }

255}

256

277static inline void \_\_sparse\_cache \*[arch\_cache\_cached\_ptr\_get](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c)(void \*ptr)

278{

279 return (\_\_sparse\_force void \_\_sparse\_cache \*)z\_xtrpoflip(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) ptr,

280 CONFIG\_XTENSA\_CACHED\_REGION,

281 CONFIG\_XTENSA\_UNCACHED\_REGION);

282}

283

302static inline void \*[arch\_cache\_uncached\_ptr\_get](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816)(void \_\_sparse\_cache \*ptr)

303{

304 return (void \*)z\_xtrpoflip((\_\_sparse\_force [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))ptr,

305 CONFIG\_XTENSA\_UNCACHED\_REGION,

306 CONFIG\_XTENSA\_CACHED\_REGION);

307}

308#else

[ 309](arch_2xtensa_2cache_8h.md#a7e8218e05aa541964a0387bbe28a40e5)static inline bool [arch\_cache\_is\_ptr\_cached](group__cache__arch__interface.md#ga9ed1c303508eb68db80f14fdb6eb7faa)(void \*ptr)

310{

311 ARG\_UNUSED(ptr);

312

313 return false;

314}

315

[ 316](arch_2xtensa_2cache_8h.md#a8098fec4edbd77142b9f94f04bc61e4e)static inline bool [arch\_cache\_is\_ptr\_uncached](group__cache__arch__interface.md#gab6bdf8089dce42e4463f761bae56e652)(void \*ptr)

317{

318 ARG\_UNUSED(ptr);

319

320 return false;

321}

322

[ 323](arch_2xtensa_2cache_8h.md#afa8a52786bd86cb3305b9a4d37c5f27c)static inline void \*[arch\_cache\_cached\_ptr\_get](group__cache__arch__interface.md#gabb31cd28a68b529ec0d7c389bb65bd9c)(void \*ptr)

324{

325 return ptr;

326}

327

[ 328](arch_2xtensa_2cache_8h.md#adf2d51455bdd6ff36609c6c68fe0fdc7)static inline void \*[arch\_cache\_uncached\_ptr\_get](group__cache__arch__interface.md#ga1b507969ecccdaf7e47b16ba190bf816)(void \*ptr)

329{

330 return ptr;

331}

332#endif

333

[ 334](arch_2xtensa_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_cache\_init](arch_2arm64_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)(void)

335{

336}

337

338

339#ifdef \_\_cplusplus

340} /\* extern "C" \*/

341#endif

342

343#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_CACHE\_H\_ \*/

[arch\_cache\_init](arch_2arm64_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)

static ALWAYS\_INLINE void arch\_cache\_init(void)

**Definition** cache.h:239

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

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

[ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)

#define ROUND\_DOWN(x, align)

Value of x rounded down to the previous multiple of align.

**Definition** util.h:329

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[sparse.h](sparse_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [cache.h](arch_2xtensa_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
