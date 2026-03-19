---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys_2util_8h_source.html
original_path: doxygen/html/sys_2util_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util.h

[Go to the documentation of this file.](sys_2util_8h.md)

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

[ 33](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)#define NUM\_BITS(t) (sizeof(t) \* BITS\_PER\_BYTE)

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

[ 61](group__sys-util.md#ga369ecd38b3ab077fc235f892354bb46f)#define BITS\_PER\_BYTE (\_\_CHAR\_BIT\_\_)

62

[ 64](group__sys-util.md#gae162e1c2f985d37fff7d41f42ed65a6e)#define BITS\_PER\_NIBBLE (\_\_CHAR\_BIT\_\_ / 2)

65

[ 67](group__sys-util.md#ga310d08124d6b119af05d75fe0ec0eb8c)#define NIBBLES\_PER\_BYTE (BITS\_PER\_BYTE / BITS\_PER\_NIBBLE)

68

[ 70](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)#define BITS\_PER\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_)

71

[ 73](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891)#define BITS\_PER\_LONG\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_)

74

[ 79](group__sys-util.md#ga58530d20924859d16358c7400c37738d)#define GENMASK(h, l) \

80 (((~0UL) - (1UL << (l)) + 1) & (~0UL >> (BITS\_PER\_LONG - 1 - (h))))

81

[ 86](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)#define GENMASK64(h, l) \

87 (((~0ULL) - (1ULL << (l)) + 1) & (~0ULL >> (BITS\_PER\_LONG\_LONG - 1 - (h))))

88

[ 90](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)#define ZERO\_OR\_COMPILE\_ERROR(cond) ((int) sizeof(char[1 - 2 \* !(cond)]) - 1)

91

92#if defined(\_\_cplusplus)

93

94/\* The built-in function used below for type checking in C is not

95 \* supported by GNU C++.

96 \*/

97#define ARRAY\_SIZE(array) (sizeof(array) / sizeof((array)[0]))

98

99#else /\* \_\_cplusplus \*/

100

[ 106](group__sys-util.md#gaa0be479debd8300ab6b43f4d028ab5da)#define IS\_ARRAY(array) \

107 ZERO\_OR\_COMPILE\_ERROR( \

108 !\_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(array), \

109 \_\_typeof\_\_(&(array)[0])))

110

[ 120](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)#define ARRAY\_SIZE(array) \

121 ((size\_t) (IS\_ARRAY(array) + (sizeof(array) / sizeof((array)[0]))))

122

123#endif /\* \_\_cplusplus \*/

124

[ 142](group__sys-util.md#gac36718df45178ad9de50f6e0b8d75d7e)#define FLEXIBLE\_ARRAY\_DECLARE(type, name) \

143 struct { \

144 struct { } \_\_unused\_##name; \

145 type name[]; \

146 }

147

[ 162](group__sys-util.md#gad403257ac6868c8bf3415ae771ce0a04)#define IS\_ARRAY\_ELEMENT(array, ptr) \

163 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

164 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]) && \

165 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) % sizeof((array)[0]) == 0)

166

[ 181](group__sys-util.md#ga27c31909224761e41d77118b41212d6b)#define ARRAY\_INDEX(array, ptr) \

182 ({ \

183 \_\_ASSERT\_NO\_MSG(IS\_ARRAY\_ELEMENT(array, ptr)); \

184 (\_\_typeof\_\_((array)[0]) \*)(ptr) - (array); \

185 })

186

[ 197](group__sys-util.md#ga4fbecf59c021cb60fa1267b7818f90ef)#define PART\_OF\_ARRAY(array, ptr) \

198 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

199 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]))

200

[ 218](group__sys-util.md#gae0516bf7a39795bcc6f0dfbf3a180c05)#define ARRAY\_INDEX\_FLOOR(array, ptr) \

219 ({ \

220 \_\_ASSERT\_NO\_MSG(PART\_OF\_ARRAY(array, ptr)); \

221 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) / sizeof((array)[0]); \

222 })

223

[ 230](group__sys-util.md#ga7a1647a1d17185f9438ed0e3096e68bc)#define ARRAY\_FOR\_EACH(array, idx) for (size\_t idx = 0; (idx) < ARRAY\_SIZE(array); ++(idx))

231

[ 238](group__sys-util.md#gafd9d42bbb945424f11b7b023dfd519f9)#define ARRAY\_FOR\_EACH\_PTR(array, ptr) \

239 for (\_\_typeof\_\_(\*(array)) \*ptr = (array); (size\_t)((ptr) - (array)) < ARRAY\_SIZE(array); \

240 ++(ptr))

241

[ 249](group__sys-util.md#ga78e587047fe4af679141595363c07179)#define SAME\_TYPE(a, b) \_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(a), \_\_typeof\_\_(b))

250

254#ifndef \_\_cplusplus

[ 255](group__sys-util.md#gaf2279c11f90f7461a417f9646af7dc5c)#define CONTAINER\_OF\_VALIDATE(ptr, type, field) \

256 BUILD\_ASSERT(SAME\_TYPE(\*(ptr), ((type \*)0)->field) || \

257 SAME\_TYPE(\*(ptr), void), \

258 "pointer type mismatch in CONTAINER\_OF");

259#else

260#define CONTAINER\_OF\_VALIDATE(ptr, type, field)

261#endif

262

[ 284](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)#define CONTAINER\_OF(ptr, type, field) \

285 ({ \

286 CONTAINER\_OF\_VALIDATE(ptr, type, field) \

287 ((type \*)(((char \*)(ptr)) - offsetof(type, field))); \

288 })

289

[ 298](group__sys-util.md#ga78c188c333605984c4c83f80d15092a4)#define SIZEOF\_FIELD(type, member) sizeof((((type \*)0)->member))

299

[ 311](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)#define CONCAT(...) \

312 UTIL\_CAT(\_CONCAT\_, NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

313

[ 317](group__sys-util.md#gabf601ce26a569512a4e422a074934660)#define IS\_ALIGNED(ptr, align) (((uintptr\_t)(ptr)) % (align) == 0)

318

[ 322](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)#define ROUND\_UP(x, align) \

323 ((((unsigned long)(x) + ((unsigned long)(align) - 1)) / \

324 (unsigned long)(align)) \* (unsigned long)(align))

325

[ 329](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)#define ROUND\_DOWN(x, align) \

330 (((unsigned long)(x) / (unsigned long)(align)) \* (unsigned long)(align))

331

[ 333](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)#define WB\_UP(x) ROUND\_UP(x, sizeof(void \*))

334

[ 336](group__sys-util.md#gadbc789ee99633a92584387ba2a4f7052)#define WB\_DN(x) ROUND\_DOWN(x, sizeof(void \*))

337

[ 352](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)#define DIV\_ROUND\_UP(n, d) (((n) + (d) - 1) / (d))

353

[ 369](group__sys-util.md#ga57fc13eb777500b3e22d3ff457cfd0d7)#define DIV\_ROUND\_CLOSEST(n, d) \

370 (((((\_\_typeof\_\_(n))-1) < 0) && (((\_\_typeof\_\_(d))-1) < 0) && ((n) < 0) ^ ((d) < 0)) \

371 ? ((n) - ((d) / 2)) / (d) \

372 : ((n) + ((d) / 2)) / (d))

373

374#ifndef MAX

[ 386](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)#define MAX(a, b) (((a) > (b)) ? (a) : (b))

387#endif

388

389#ifndef MIN

[ 401](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)#define MIN(a, b) (((a) < (b)) ? (a) : (b))

402#endif

403

404#ifndef CLAMP

[ 417](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)#define CLAMP(val, low, high) (((val) <= (low)) ? (low) : MIN(val, high))

418#endif

419

[ 432](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)#define IN\_RANGE(val, min, max) ((val) >= (min) && (val) <= (max))

433

[ 439](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)static inline bool [is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)(unsigned int x)

440{

441 return [IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(x);

442}

443

[ 463](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [is\_null\_no\_warn](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366)(void \*p)

464{

465 return p == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

466}

467

[ 475](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift)

476{

477 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sign\_ext;

478

479 if (shift == 0U) {

480 return value;

481 }

482

483 /\* extract sign bit \*/

484 sign\_ext = (value >> 63) & 1;

485

486 /\* make all bits of sign\_ext be the same as the value's sign bit \*/

487 sign\_ext = -sign\_ext;

488

489 /\* shift value and fill opened bit positions with sign bit \*/

490 return (value >> shift) | (sign\_ext << (64 - shift));

491}

492

[ 502](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)static inline void [bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)(void \*dst, const void \*src, size\_t size)

503{

504 size\_t i;

505

506 for (i = 0; i < size; ++i) {

507 ((volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)dst)[i] = ((volatile const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)src)[i];

508 }

509}

510

[ 521](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)static inline void [byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)(void \*a, void \*b, size\_t size)

522{

523 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) t;

524 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)a;

525 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bb = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)b;

526

527 for (; size > 0; --size) {

528 t = \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b);

529 \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)++ = \*bb;

530 \*bb++ = t;

531 }

532}

533

[ 542](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)int [char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)(char c, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*x);

543

[ 552](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)int [hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x, char \*c);

553

[ 564](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)size\_t [bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen, char \*hex, size\_t hexlen);

565

[ 576](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)size\_t [hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)(const char \*hex, size\_t hexlen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

577

[ 585](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd)

586{

587 return ((10 \* (bcd >> 4)) + (bcd & 0x0F));

588}

589

[ 597](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin)

598{

599 return (((bin / 10) << 4) | (bin % 10));

600}

601

[ 615](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)(char \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buflen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

616

[ 623](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sign\_extend](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index)

624{

625 \_\_ASSERT\_NO\_MSG(index <= 31);

626

627 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift = 31 - index;

628

629 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(value << shift) >> shift;

630}

631

[ 638](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sign\_extend\_64](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index)

639{

640 \_\_ASSERT\_NO\_MSG(index <= 63);

641

642 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift = 63 - index;

643

644 return ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))(value << shift) >> shift;

645}

646

[ 671](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)char \*[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)(char \*utf8\_str);

672

[ 687](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)char \*[utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)(char \*dst, const char \*src, size\_t n);

688

689#define \_\_z\_log2d(x) (32 - \_\_builtin\_clz(x) - 1)

690#define \_\_z\_log2q(x) (64 - \_\_builtin\_clzll(x) - 1)

691#define \_\_z\_log2(x) (sizeof(\_\_typeof\_\_(x)) > 4 ? \_\_z\_log2q(x) : \_\_z\_log2d(x))

692

[ 703](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)#define LOG2(x) ((x) < 1 ? -1 : \_\_z\_log2(x))

704

[ 715](group__sys-util.md#gada629edfcec9fa2fc3dc5d7af70abb03)#define LOG2CEIL(x) ((x) <= 1 ? 0 : \_\_z\_log2((x)-1) + 1)

716

[ 729](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)#define NHPOT(x) ((x) < 1 ? 1 : ((x) > (1ULL<<63) ? 0 : 1ULL << LOG2CEIL(x)))

730

743#define Z\_DETECT\_POINTER\_OVERFLOW(addr, buflen) \

744 (((buflen) != 0) && \

745 ((UINTPTR\_MAX - (uintptr\_t)(addr)) <= ((uintptr\_t)((buflen) - 1))))

746

[ 755](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)static inline void [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src2, size\_t len)

756{

757 while (len--) {

758 \*dst++ = \*src1++ ^ \*src2++;

759 }

760}

761

[ 769](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)static inline void [mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[4])

770{

771 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 4U);

772}

773

[ 781](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)static inline void [mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[16])

782{

783 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 16);

784}

785

786#ifdef \_\_cplusplus

787}

788#endif

789

790/\* This file must be included at the end of the !\_ASMLANGUAGE guard.

791 \* It depends on macros defined in this file above which cannot be forward declared.

792 \*/

793#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

794

795#endif /\* !\_ASMLANGUAGE \*/

796

798#ifdef \_LINKER

799/\* This is used in linker scripts so need to avoid type casting there \*/

[ 800](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)#define KB(x) ((x) << 10)

801#else

802#define KB(x) (((size\_t)(x)) << 10)

803#endif

[ 805](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)#define MB(x) (KB(x) << 10)

[ 807](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)#define GB(x) (MB(x) << 10)

808

[ 810](group__sys-util.md#gaee55275295c076c6d23c994777623253)#define KHZ(x) ((x) \* 1000)

[ 812](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)#define MHZ(x) (KHZ(x) \* 1000)

813

826#if defined(CONFIG\_ARCH\_POSIX)

827#define Z\_SPIN\_DELAY(t) k\_busy\_wait(t)

828#else

829#define Z\_SPIN\_DELAY(t)

830#endif

831

[ 847](group__sys-util.md#ga68eb35df6b4715714312df90209accee)#define WAIT\_FOR(expr, timeout, delay\_stmt) \

848 ({ \

849 uint32\_t \_wf\_cycle\_count = k\_us\_to\_cyc\_ceil32(timeout); \

850 uint32\_t \_wf\_start = k\_cycle\_get\_32(); \

851 while (!(expr) && (\_wf\_cycle\_count > (k\_cycle\_get\_32() - \_wf\_start))) { \

852 delay\_stmt; \

853 Z\_SPIN\_DELAY(10); \

854 } \

855 (expr); \

856 })

857

861

862#endif /\* ZEPHYR\_INCLUDE\_SYS\_UTIL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)

irp nz macro MOVR cc s mov cc s endm endr irp aa

**Definition** asm-macro-32-bit-gnu.h:16

[sign\_extend\_64](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f)

static int64\_t sign\_extend\_64(uint64\_t value, uint8\_t index)

Sign extend a 64 bit value using the index bit as sign bit.

**Definition** util.h:638

[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)

char \* utf8\_trunc(char \*utf8\_str)

Properly truncate a NULL-terminated UTF-8 string.

[arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)

static int64\_t arithmetic\_shift\_right(int64\_t value, uint8\_t shift)

Arithmetic shift right.

**Definition** util.h:475

[hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)

size\_t hex2bin(const char \*hex, size\_t hexlen, uint8\_t \*buf, size\_t buflen)

Convert a hexadecimal string into a binary array.

[bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)

static void bytecpy(void \*dst, const void \*src, size\_t size)

byte by byte memcpy.

**Definition** util.h:502

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

**Definition** util.h:463

[mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)

static void mem\_xor\_128(uint8\_t dst[16], const uint8\_t src1[16], const uint8\_t src2[16])

XOR 128 bits.

**Definition** util.h:781

[bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)

static uint8\_t bin2bcd(uint8\_t bin)

Convert a binary value to binary coded decimal (BCD 8421).

**Definition** util.h:597

[mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)

static void mem\_xor\_32(uint8\_t dst[4], const uint8\_t src1[4], const uint8\_t src2[4])

XOR 32 bits.

**Definition** util.h:769

[byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)

static void byteswp(void \*a, void \*b, size\_t size)

byte by byte swap.

**Definition** util.h:521

[mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)

static void mem\_xor\_n(uint8\_t \*dst, const uint8\_t \*src1, const uint8\_t \*src2, size\_t len)

XOR n bytes.

**Definition** util.h:755

[hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)

int hex2char(uint8\_t x, char \*c)

Convert a single hexadecimal nibble into a character.

[bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)

static uint8\_t bcd2bin(uint8\_t bcd)

Convert a binary coded decimal (BCD 8421) value to binary.

**Definition** util.h:585

[char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)

int char2hex(char c, uint8\_t \*x)

Convert a single character into a hexadecimal nibble.

[u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)

uint8\_t u8\_to\_dec(char \*buf, uint8\_t buflen, uint8\_t value)

Convert a uint8\_t into a decimal string representation.

[is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)

static bool is\_power\_of\_two(unsigned int x)

Is x a power of two?

**Definition** util.h:439

[sign\_extend](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee)

static int32\_t sign\_extend(uint32\_t value, uint8\_t index)

Sign extend an 8, 16 or 32 bit value using the index bit as sign bit.

**Definition** util.h:623

[bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)

size\_t bin2hex(const uint8\_t \*buf, size\_t buflen, char \*hex, size\_t hexlen)

Convert a binary array into string representation.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

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
- [util.h](sys_2util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
