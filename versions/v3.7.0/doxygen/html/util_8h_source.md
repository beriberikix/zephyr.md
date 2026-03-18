---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/util_8h_source.html
original_path: doxygen/html/util_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util.h

[Go to the documentation of this file.](util_8h.md)

1/\*

2 \* Copyright (c) 2011-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_SYS\_UTIL\_H\_

15#define ZEPHYR\_INCLUDE\_SYS\_UTIL\_H\_

16

17#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

18#include <[zephyr/toolchain.h](toolchain_8h.md)>

19

20/\* needs to be outside \_ASMLANGUAGE so 'true' and 'false' can turn

21 \* into '1' and '0' for asm or linker scripts

22 \*/

23#include <[stdbool.h](stdbool_8h.md)>

24

25#ifndef \_ASMLANGUAGE

26

27#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <stddef.h>

30#include <[stdint.h](stdint_8h.md)>

31

[ 33](util_8h.md#afa27c06d0ad6b949289431ad75f104ab)#define NUM\_BITS(t) (sizeof(t) \* 8)

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

46

[ 48](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)#define POINTER\_TO\_UINT(x) ((uintptr\_t) (x))

[ 50](group__sys-util.md#gab74ce0513c348e0b257d38473e77e1a1)#define UINT\_TO\_POINTER(x) ((void \*) (uintptr\_t) (x))

[ 52](group__sys-util.md#ga6e5ec9c46d0140315a7c1d80d1cc3c38)#define POINTER\_TO\_INT(x) ((intptr\_t) (x))

[ 54](group__sys-util.md#gae236ed18fe2ff18ab47c15d2e7eeb417)#define INT\_TO\_POINTER(x) ((void \*) (intptr\_t) (x))

55

56#if !(defined(\_\_CHAR\_BIT\_\_) && defined(\_\_SIZEOF\_LONG\_\_) && defined(\_\_SIZEOF\_LONG\_LONG\_\_))

57# error Missing required predefined macros for BITS\_PER\_LONG calculation

58#endif

59

[ 61](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)#define BITS\_PER\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_)

62

[ 64](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891)#define BITS\_PER\_LONG\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_)

65

[ 70](group__sys-util.md#ga58530d20924859d16358c7400c37738d)#define GENMASK(h, l) \

71 (((~0UL) - (1UL << (l)) + 1) & (~0UL >> (BITS\_PER\_LONG - 1 - (h))))

72

[ 77](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)#define GENMASK64(h, l) \

78 (((~0ULL) - (1ULL << (l)) + 1) & (~0ULL >> (BITS\_PER\_LONG\_LONG - 1 - (h))))

79

[ 81](group__sys-util.md#ga92235ab2e350fbdc01ddf0f894e5e4c0)#define LSB\_GET(value) ((value) & -(value))

82

[ 87](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)#define FIELD\_GET(mask, value) (((value) & (mask)) / LSB\_GET(mask))

88

[ 94](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)#define FIELD\_PREP(mask, value) (((value) \* LSB\_GET(mask)) & (mask))

95

[ 97](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)#define ZERO\_OR\_COMPILE\_ERROR(cond) ((int) sizeof(char[1 - 2 \* !(cond)]) - 1)

98

99#if defined(\_\_cplusplus)

100

101/\* The built-in function used below for type checking in C is not

102 \* supported by GNU C++.

103 \*/

104#define ARRAY\_SIZE(array) (sizeof(array) / sizeof((array)[0]))

105

106#else /\* \_\_cplusplus \*/

107

[ 113](group__sys-util.md#gaa0be479debd8300ab6b43f4d028ab5da)#define IS\_ARRAY(array) \

114 ZERO\_OR\_COMPILE\_ERROR( \

115 !\_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(array), \

116 \_\_typeof\_\_(&(array)[0])))

117

[ 127](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)#define ARRAY\_SIZE(array) \

128 ((size\_t) (IS\_ARRAY(array) + (sizeof(array) / sizeof((array)[0]))))

129

130#endif /\* \_\_cplusplus \*/

131

[ 146](group__sys-util.md#gad403257ac6868c8bf3415ae771ce0a04)#define IS\_ARRAY\_ELEMENT(array, ptr) \

147 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

148 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]) && \

149 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) % sizeof((array)[0]) == 0)

150

[ 165](group__sys-util.md#ga27c31909224761e41d77118b41212d6b)#define ARRAY\_INDEX(array, ptr) \

166 ({ \

167 \_\_ASSERT\_NO\_MSG(IS\_ARRAY\_ELEMENT(array, ptr)); \

168 (\_\_typeof\_\_((array)[0]) \*)(ptr) - (array); \

169 })

170

[ 181](group__sys-util.md#ga4fbecf59c021cb60fa1267b7818f90ef)#define PART\_OF\_ARRAY(array, ptr) \

182 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

183 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]))

184

[ 202](group__sys-util.md#gae0516bf7a39795bcc6f0dfbf3a180c05)#define ARRAY\_INDEX\_FLOOR(array, ptr) \

203 ({ \

204 \_\_ASSERT\_NO\_MSG(PART\_OF\_ARRAY(array, ptr)); \

205 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) / sizeof((array)[0]); \

206 })

207

[ 214](group__sys-util.md#ga7a1647a1d17185f9438ed0e3096e68bc)#define ARRAY\_FOR\_EACH(array, idx) for (size\_t idx = 0; (idx) < ARRAY\_SIZE(array); ++(idx))

215

[ 222](group__sys-util.md#gafd9d42bbb945424f11b7b023dfd519f9)#define ARRAY\_FOR\_EACH\_PTR(array, ptr) \

223 for (\_\_typeof\_\_(\*(array)) \*ptr = (array); (size\_t)((ptr) - (array)) < ARRAY\_SIZE(array); \

224 ++(ptr))

225

[ 233](group__sys-util.md#ga78e587047fe4af679141595363c07179)#define SAME\_TYPE(a, b) \_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(a), \_\_typeof\_\_(b))

234

238#ifndef \_\_cplusplus

[ 239](group__sys-util.md#gaf2279c11f90f7461a417f9646af7dc5c)#define CONTAINER\_OF\_VALIDATE(ptr, type, field) \

240 BUILD\_ASSERT(SAME\_TYPE(\*(ptr), ((type \*)0)->field) || \

241 SAME\_TYPE(\*(ptr), void), \

242 "pointer type mismatch in CONTAINER\_OF");

243#else

244#define CONTAINER\_OF\_VALIDATE(ptr, type, field)

245#endif

246

[ 268](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)#define CONTAINER\_OF(ptr, type, field) \

269 ({ \

270 CONTAINER\_OF\_VALIDATE(ptr, type, field) \

271 ((type \*)(((char \*)(ptr)) - offsetof(type, field))); \

272 })

273

[ 282](group__sys-util.md#ga78c188c333605984c4c83f80d15092a4)#define SIZEOF\_FIELD(type, member) sizeof((((type \*)0)->member))

283

[ 295](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)#define CONCAT(...) \

296 UTIL\_CAT(\_CONCAT\_, NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

297

[ 301](group__sys-util.md#gabf601ce26a569512a4e422a074934660)#define IS\_ALIGNED(ptr, align) (((uintptr\_t)(ptr)) % (align) == 0)

302

[ 306](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)#define ROUND\_UP(x, align) \

307 ((((unsigned long)(x) + ((unsigned long)(align) - 1)) / \

308 (unsigned long)(align)) \* (unsigned long)(align))

309

[ 313](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)#define ROUND\_DOWN(x, align) \

314 (((unsigned long)(x) / (unsigned long)(align)) \* (unsigned long)(align))

315

[ 317](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)#define WB\_UP(x) ROUND\_UP(x, sizeof(void \*))

318

[ 320](group__sys-util.md#gadbc789ee99633a92584387ba2a4f7052)#define WB\_DN(x) ROUND\_DOWN(x, sizeof(void \*))

321

[ 336](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)#define DIV\_ROUND\_UP(n, d) (((n) + (d) - 1) / (d))

337

[ 353](group__sys-util.md#ga57fc13eb777500b3e22d3ff457cfd0d7)#define DIV\_ROUND\_CLOSEST(n, d) \

354 ((((n) < 0) ^ ((d) < 0)) ? ((n) - ((d) / 2)) / (d) : \

355 ((n) + ((d) / 2)) / (d))

356

[ 361](group__sys-util.md#gaad408461e7ab356650bcd5c83bc0ed39)#define ceiling\_fraction(numerator, divider) \_\_DEPRECATED\_MACRO \

362 DIV\_ROUND\_UP(numerator, divider)

363

364#ifndef MAX

[ 376](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)#define MAX(a, b) (((a) > (b)) ? (a) : (b))

377#endif

378

379#ifndef MIN

[ 391](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)#define MIN(a, b) (((a) < (b)) ? (a) : (b))

392#endif

393

394#ifndef CLAMP

[ 407](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)#define CLAMP(val, low, high) (((val) <= (low)) ? (low) : MIN(val, high))

408#endif

409

[ 422](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)#define IN\_RANGE(val, min, max) ((val) >= (min) && (val) <= (max))

423

[ 429](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)static inline bool [is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)(unsigned int x)

430{

431 return [IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(x);

432}

433

[ 453](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [is\_null\_no\_warn](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366)(void \*p)

454{

455 return p == NULL;

456}

457

[ 465](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift)

466{

467 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sign\_ext;

468

469 if (shift == 0U) {

470 return value;

471 }

472

473 /\* extract sign bit \*/

474 sign\_ext = (value >> 63) & 1;

475

476 /\* make all bits of sign\_ext be the same as the value's sign bit \*/

477 sign\_ext = -sign\_ext;

478

479 /\* shift value and fill opened bit positions with sign bit \*/

480 return (value >> shift) | (sign\_ext << (64 - shift));

481}

482

[ 492](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)static inline void [bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)(void \*dst, const void \*src, size\_t size)

493{

494 size\_t i;

495

496 for (i = 0; i < size; ++i) {

497 ((volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)dst)[i] = ((volatile const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)src)[i];

498 }

499}

500

[ 511](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)static inline void [byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)(void \*a, void \*b, size\_t size)

512{

513 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) t;

514 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)a;

515 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bb = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)b;

516

517 for (; size > 0; --size) {

518 t = \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b);

519 \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)++ = \*bb;

520 \*bb++ = t;

521 }

522}

523

[ 532](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)int [char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)(char c, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*x);

533

[ 542](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)int [hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x, char \*c);

543

[ 554](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)size\_t [bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen, char \*hex, size\_t hexlen);

555

[ 566](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)size\_t [hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)(const char \*hex, size\_t hexlen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

567

[ 575](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd)

576{

577 return ((10 \* (bcd >> 4)) + (bcd & 0x0F));

578}

579

[ 587](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin)

588{

589 return (((bin / 10) << 4) | (bin % 10));

590}

591

[ 605](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)(char \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buflen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

606

[ 613](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sign\_extend](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index)

614{

615 \_\_ASSERT\_NO\_MSG(index <= 31);

616

617 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift = 31 - index;

618

619 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(value << shift) >> shift;

620}

621

[ 628](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sign\_extend\_64](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index)

629{

630 \_\_ASSERT\_NO\_MSG(index <= 63);

631

632 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift = 63 - index;

633

634 return ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))(value << shift) >> shift;

635}

636

[ 661](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)char \*[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)(char \*utf8\_str);

662

[ 677](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)char \*[utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)(char \*dst, const char \*src, size\_t n);

678

679#define \_\_z\_log2d(x) (32 - \_\_builtin\_clz(x) - 1)

680#define \_\_z\_log2q(x) (64 - \_\_builtin\_clzll(x) - 1)

681#define \_\_z\_log2(x) (sizeof(\_\_typeof\_\_(x)) > 4 ? \_\_z\_log2q(x) : \_\_z\_log2d(x))

682

[ 693](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)#define LOG2(x) ((x) < 1 ? -1 : \_\_z\_log2(x))

694

[ 705](group__sys-util.md#gada629edfcec9fa2fc3dc5d7af70abb03)#define LOG2CEIL(x) ((x) < 1 ? 0 : \_\_z\_log2((x)-1) + 1)

706

[ 719](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)#define NHPOT(x) ((x) < 1 ? 1 : ((x) > (1ULL<<63) ? 0 : 1ULL << LOG2CEIL(x)))

720

733#define Z\_DETECT\_POINTER\_OVERFLOW(addr, buflen) \

734 (((buflen) != 0) && \

735 ((UINTPTR\_MAX - (uintptr\_t)(addr)) <= ((uintptr\_t)((buflen) - 1))))

736

[ 745](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)static inline void [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src2, size\_t len)

746{

747 while (len--) {

748 \*dst++ = \*src1++ ^ \*src2++;

749 }

750}

751

[ 759](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)static inline void [mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[4])

760{

761 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 4U);

762}

763

[ 771](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)static inline void [mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[16])

772{

773 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 16);

774}

775

776#ifdef \_\_cplusplus

777}

778#endif

779

780/\* This file must be included at the end of the !\_ASMLANGUAGE guard.

781 \* It depends on macros defined in this file above which cannot be forward declared.

782 \*/

783#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

784

785#endif /\* !\_ASMLANGUAGE \*/

786

788#ifdef \_LINKER

789/\* This is used in linker scripts so need to avoid type casting there \*/

[ 790](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)#define KB(x) ((x) << 10)

791#else

792#define KB(x) (((size\_t)(x)) << 10)

793#endif

[ 795](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)#define MB(x) (KB(x) << 10)

[ 797](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)#define GB(x) (MB(x) << 10)

798

[ 800](group__sys-util.md#gaee55275295c076c6d23c994777623253)#define KHZ(x) ((x) \* 1000)

[ 802](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)#define MHZ(x) (KHZ(x) \* 1000)

803

816#if defined(CONFIG\_ARCH\_POSIX)

817#define Z\_SPIN\_DELAY(t) k\_busy\_wait(t)

818#else

819#define Z\_SPIN\_DELAY(t)

820#endif

821

[ 837](group__sys-util.md#ga68eb35df6b4715714312df90209accee)#define WAIT\_FOR(expr, timeout, delay\_stmt) \

838 ({ \

839 uint32\_t \_wf\_cycle\_count = k\_us\_to\_cyc\_ceil32(timeout); \

840 uint32\_t \_wf\_start = k\_cycle\_get\_32(); \

841 while (!(expr) && (\_wf\_cycle\_count > (k\_cycle\_get\_32() - \_wf\_start))) { \

842 delay\_stmt; \

843 Z\_SPIN\_DELAY(10); \

844 } \

845 (expr); \

846 })

847

851

852#endif /\* ZEPHYR\_INCLUDE\_SYS\_UTIL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)

irp nz macro MOVR cc s mov cc s endm endr irp aa

**Definition** asm-macro-32-bit-gnu.h:16

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[sign\_extend\_64](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)

static int64\_t sign\_extend\_64(uint64\_t value, uint8\_t index)

Sign extend a 64 bit value using the index bit as sign bit.

**Definition** util.h:628

[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)

char \* utf8\_trunc(char \*utf8\_str)

Properly truncate a NULL-terminated UTF-8 string.

[arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)

static int64\_t arithmetic\_shift\_right(int64\_t value, uint8\_t shift)

Arithmetic shift right.

**Definition** util.h:465

[hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)

size\_t hex2bin(const char \*hex, size\_t hexlen, uint8\_t \*buf, size\_t buflen)

Convert a hexadecimal string into a binary array.

[bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)

static void bytecpy(void \*dst, const void \*src, size\_t size)

byte by byte memcpy.

**Definition** util.h:492

[utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)

char \* utf8\_lcpy(char \*dst, const char \*src, size\_t n)

Copies a UTF-8 encoded string from src to dst.

[IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)

#define IS\_POWER\_OF\_TWO(x)

Check if a x is a power of two.

**Definition** util\_macro.h:77

[is\_null\_no\_warn](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366)

static ALWAYS\_INLINE bool is\_null\_no\_warn(void \*p)

Is p equal to NULL?

**Definition** util.h:453

[mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)

static void mem\_xor\_128(uint8\_t dst[16], const uint8\_t src1[16], const uint8\_t src2[16])

XOR 128 bits.

**Definition** util.h:771

[bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)

static uint8\_t bin2bcd(uint8\_t bin)

Convert a binary value to binary coded decimal (BCD 8421).

**Definition** util.h:587

[mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)

static void mem\_xor\_32(uint8\_t dst[4], const uint8\_t src1[4], const uint8\_t src2[4])

XOR 32 bits.

**Definition** util.h:759

[byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)

static void byteswp(void \*a, void \*b, size\_t size)

byte by byte swap.

**Definition** util.h:511

[mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)

static void mem\_xor\_n(uint8\_t \*dst, const uint8\_t \*src1, const uint8\_t \*src2, size\_t len)

XOR n bytes.

**Definition** util.h:745

[hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)

int hex2char(uint8\_t x, char \*c)

Convert a single hexadecimal nibble into a character.

[bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)

static uint8\_t bcd2bin(uint8\_t bcd)

Convert a binary coded decimal (BCD 8421) value to binary.

**Definition** util.h:575

[char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)

int char2hex(char c, uint8\_t \*x)

Convert a single character into a hexadecimal nibble.

[u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)

uint8\_t u8\_to\_dec(char \*buf, uint8\_t buflen, uint8\_t value)

Convert a uint8\_t into a decimal string representation.

[is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)

static bool is\_power\_of\_two(unsigned int x)

Is x a power of two?

**Definition** util.h:429

[sign\_extend](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)

static int32\_t sign\_extend(uint32\_t value, uint8\_t index)

Sign extend an 8, 16 or 32 bit value using the index bit as sign bit.

**Definition** util.h:613

[bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)

size\_t bin2hex(const uint8\_t \*buf, size\_t buflen, char \*hex, size\_t hexlen)

Convert a binary array into string representation.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[time\_units.h](time__units_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util.h](util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
