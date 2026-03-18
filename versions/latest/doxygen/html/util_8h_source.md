---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/util_8h_source.html
original_path: doxygen/html/util_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <stddef.h>

29#include <[stdint.h](stdint_8h.md)>

30

[ 32](util_8h.md#afa27c06d0ad6b949289431ad75f104ab)#define NUM\_BITS(t) (sizeof(t) \* 8)

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

43

[ 45](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)#define POINTER\_TO\_UINT(x) ((uintptr\_t) (x))

[ 47](group__sys-util.md#gab74ce0513c348e0b257d38473e77e1a1)#define UINT\_TO\_POINTER(x) ((void \*) (uintptr\_t) (x))

[ 49](group__sys-util.md#ga6e5ec9c46d0140315a7c1d80d1cc3c38)#define POINTER\_TO\_INT(x) ((intptr\_t) (x))

[ 51](group__sys-util.md#gae236ed18fe2ff18ab47c15d2e7eeb417)#define INT\_TO\_POINTER(x) ((void \*) (intptr\_t) (x))

52

53#if !(defined(\_\_CHAR\_BIT\_\_) && defined(\_\_SIZEOF\_LONG\_\_) && defined(\_\_SIZEOF\_LONG\_LONG\_\_))

54# error Missing required predefined macros for BITS\_PER\_LONG calculation

55#endif

56

[ 58](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)#define BITS\_PER\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_)

59

[ 61](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891)#define BITS\_PER\_LONG\_LONG (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_)

62

[ 67](group__sys-util.md#ga58530d20924859d16358c7400c37738d)#define GENMASK(h, l) \

68 (((~0UL) - (1UL << (l)) + 1) & (~0UL >> (BITS\_PER\_LONG - 1 - (h))))

69

[ 74](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)#define GENMASK64(h, l) \

75 (((~0ULL) - (1ULL << (l)) + 1) & (~0ULL >> (BITS\_PER\_LONG\_LONG - 1 - (h))))

76

[ 78](group__sys-util.md#ga92235ab2e350fbdc01ddf0f894e5e4c0)#define LSB\_GET(value) ((value) & -(value))

79

[ 84](group__sys-util.md#gaa49a456f06f7bdbedfcf3517e461947e)#define FIELD\_GET(mask, value) (((value) & (mask)) / LSB\_GET(mask))

85

[ 91](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)#define FIELD\_PREP(mask, value) (((value) \* LSB\_GET(mask)) & (mask))

92

[ 94](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)#define ZERO\_OR\_COMPILE\_ERROR(cond) ((int) sizeof(char[1 - 2 \* !(cond)]) - 1)

95

96#if defined(\_\_cplusplus)

97

98/\* The built-in function used below for type checking in C is not

99 \* supported by GNU C++.

100 \*/

101#define ARRAY\_SIZE(array) (sizeof(array) / sizeof((array)[0]))

102

103#else /\* \_\_cplusplus \*/

104

[ 110](group__sys-util.md#gaa0be479debd8300ab6b43f4d028ab5da)#define IS\_ARRAY(array) \

111 ZERO\_OR\_COMPILE\_ERROR( \

112 !\_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(array), \

113 \_\_typeof\_\_(&(array)[0])))

114

[ 124](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)#define ARRAY\_SIZE(array) \

125 ((size\_t) (IS\_ARRAY(array) + (sizeof(array) / sizeof((array)[0]))))

126

127#endif /\* \_\_cplusplus \*/

128

[ 143](group__sys-util.md#gad403257ac6868c8bf3415ae771ce0a04)#define IS\_ARRAY\_ELEMENT(array, ptr) \

144 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

145 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]) && \

146 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) % sizeof((array)[0]) == 0)

147

[ 162](group__sys-util.md#ga27c31909224761e41d77118b41212d6b)#define ARRAY\_INDEX(array, ptr) \

163 ({ \

164 \_\_ASSERT\_NO\_MSG(IS\_ARRAY\_ELEMENT(array, ptr)); \

165 (\_\_typeof\_\_((array)[0]) \*)(ptr) - (array); \

166 })

167

[ 178](group__sys-util.md#ga4fbecf59c021cb60fa1267b7818f90ef)#define PART\_OF\_ARRAY(array, ptr) \

179 ((ptr) && POINTER\_TO\_UINT(array) <= POINTER\_TO\_UINT(ptr) && \

180 POINTER\_TO\_UINT(ptr) < POINTER\_TO\_UINT(&(array)[ARRAY\_SIZE(array)]))

181

[ 199](group__sys-util.md#gae0516bf7a39795bcc6f0dfbf3a180c05)#define ARRAY\_INDEX\_FLOOR(array, ptr) \

200 ({ \

201 \_\_ASSERT\_NO\_MSG(PART\_OF\_ARRAY(array, ptr)); \

202 (POINTER\_TO\_UINT(ptr) - POINTER\_TO\_UINT(array)) / sizeof((array)[0]); \

203 })

204

[ 211](group__sys-util.md#ga7a1647a1d17185f9438ed0e3096e68bc)#define ARRAY\_FOR\_EACH(array, idx) for (size\_t idx = 0; (idx) < ARRAY\_SIZE(array); ++(idx))

212

[ 219](group__sys-util.md#gafd9d42bbb945424f11b7b023dfd519f9)#define ARRAY\_FOR\_EACH\_PTR(array, ptr) \

220 for (\_\_typeof\_\_(\*(array)) \*ptr = (array); (size\_t)((ptr) - (array)) < ARRAY\_SIZE(array); \

221 ++(ptr))

222

[ 230](group__sys-util.md#ga78e587047fe4af679141595363c07179)#define SAME\_TYPE(a, b) \_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(a), \_\_typeof\_\_(b))

231

235#ifndef \_\_cplusplus

[ 236](group__sys-util.md#gaf2279c11f90f7461a417f9646af7dc5c)#define CONTAINER\_OF\_VALIDATE(ptr, type, field) \

237 BUILD\_ASSERT(SAME\_TYPE(\*(ptr), ((type \*)0)->field) || \

238 SAME\_TYPE(\*(ptr), void), \

239 "pointer type mismatch in CONTAINER\_OF");

240#else

241#define CONTAINER\_OF\_VALIDATE(ptr, type, field)

242#endif

243

[ 265](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)#define CONTAINER\_OF(ptr, type, field) \

266 ({ \

267 CONTAINER\_OF\_VALIDATE(ptr, type, field) \

268 ((type \*)(((char \*)(ptr)) - offsetof(type, field))); \

269 })

270

[ 282](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)#define CONCAT(...) \

283 UTIL\_CAT(\_CONCAT\_, NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

284

[ 288](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)#define ROUND\_UP(x, align) \

289 ((((unsigned long)(x) + ((unsigned long)(align) - 1)) / \

290 (unsigned long)(align)) \* (unsigned long)(align))

291

[ 295](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)#define ROUND\_DOWN(x, align) \

296 (((unsigned long)(x) / (unsigned long)(align)) \* (unsigned long)(align))

297

[ 299](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)#define WB\_UP(x) ROUND\_UP(x, sizeof(void \*))

300

[ 302](group__sys-util.md#gadbc789ee99633a92584387ba2a4f7052)#define WB\_DN(x) ROUND\_DOWN(x, sizeof(void \*))

303

[ 318](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)#define DIV\_ROUND\_UP(n, d) (((n) + (d) - 1) / (d))

319

[ 335](group__sys-util.md#ga57fc13eb777500b3e22d3ff457cfd0d7)#define DIV\_ROUND\_CLOSEST(n, d) \

336 ((((n) < 0) ^ ((d) < 0)) ? ((n) - ((d) / 2)) / (d) : \

337 ((n) + ((d) / 2)) / (d))

338

[ 343](group__sys-util.md#gaad408461e7ab356650bcd5c83bc0ed39)#define ceiling\_fraction(numerator, divider) \_\_DEPRECATED\_MACRO \

344 DIV\_ROUND\_UP(numerator, divider)

345

346#ifndef MAX

[ 358](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)#define MAX(a, b) (((a) > (b)) ? (a) : (b))

359#endif

360

361#ifndef MIN

[ 373](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)#define MIN(a, b) (((a) < (b)) ? (a) : (b))

374#endif

375

376#ifndef CLAMP

[ 389](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)#define CLAMP(val, low, high) (((val) <= (low)) ? (low) : MIN(val, high))

390#endif

391

[ 404](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)#define IN\_RANGE(val, min, max) ((val) >= (min) && (val) <= (max))

405

[ 411](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)static inline bool [is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)(unsigned int x)

412{

413 return [IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(x);

414}

415

[ 423](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift)

424{

425 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) sign\_ext;

426

427 if (shift == 0U) {

428 return value;

429 }

430

431 /\* extract sign bit \*/

432 sign\_ext = (value >> 63) & 1;

433

434 /\* make all bits of sign\_ext be the same as the value's sign bit \*/

435 sign\_ext = -sign\_ext;

436

437 /\* shift value and fill opened bit positions with sign bit \*/

438 return (value >> shift) | (sign\_ext << (64 - shift));

439}

440

[ 450](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)static inline void [bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)(void \*dst, const void \*src, size\_t size)

451{

452 size\_t i;

453

454 for (i = 0; i < size; ++i) {

455 ((volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)dst)[i] = ((volatile const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)src)[i];

456 }

457}

458

[ 469](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)static inline void [byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)(void \*a, void \*b, size\_t size)

470{

471 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) t;

472 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)a;

473 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bb = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)b;

474

475 for (; size > 0; --size) {

476 t = \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b);

477 \*[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)++ = \*bb;

478 \*bb++ = t;

479 }

480}

481

[ 490](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)int [char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)(char c, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*x);

491

[ 500](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)int [hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x, char \*c);

501

[ 512](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)size\_t [bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen, char \*hex, size\_t hexlen);

513

[ 524](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)size\_t [hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)(const char \*hex, size\_t hexlen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

525

[ 533](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd)

534{

535 return ((10 \* (bcd >> 4)) + (bcd & 0x0F));

536}

537

[ 545](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin)

546{

547 return (((bin / 10) << 4) | (bin % 10));

548}

549

[ 563](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)(char \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buflen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

564

[ 589](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)char \*[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)(char \*utf8\_str);

590

[ 605](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)char \*[utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)(char \*dst, const char \*src, size\_t n);

606

607#define \_\_z\_log2d(x) (32 - \_\_builtin\_clz(x) - 1)

608#define \_\_z\_log2q(x) (64 - \_\_builtin\_clzll(x) - 1)

609#define \_\_z\_log2(x) (sizeof(\_\_typeof\_\_(x)) > 4 ? \_\_z\_log2q(x) : \_\_z\_log2d(x))

610

[ 621](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)#define LOG2(x) ((x) < 1 ? -1 : \_\_z\_log2(x))

622

[ 633](group__sys-util.md#gada629edfcec9fa2fc3dc5d7af70abb03)#define LOG2CEIL(x) ((x) < 1 ? 0 : \_\_z\_log2((x)-1) + 1)

634

[ 647](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)#define NHPOT(x) ((x) < 1 ? 1 : ((x) > (1ULL<<63) ? 0 : 1ULL << LOG2CEIL(x)))

648

661#define Z\_DETECT\_POINTER\_OVERFLOW(addr, buflen) \

662 (((buflen) != 0) && \

663 ((UINTPTR\_MAX - (uintptr\_t)(addr)) <= ((uintptr\_t)((buflen) - 1))))

664

[ 673](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)static inline void [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src2, size\_t len)

674{

675 while (len--) {

676 \*dst++ = \*src1++ ^ \*src2++;

677 }

678}

679

[ 687](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)static inline void [mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[4])

688{

689 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 4U);

690}

691

[ 699](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)static inline void [mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[16])

700{

701 [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)(dst, src1, src2, 16);

702}

703

704#ifdef \_\_cplusplus

705}

706#endif

707

708/\* This file must be included at the end of the !\_ASMLANGUAGE guard.

709 \* It depends on macros defined in this file above which cannot be forward declared.

710 \*/

711#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

712

713#endif /\* !\_ASMLANGUAGE \*/

714

716#ifdef \_LINKER

717/\* This is used in linker scripts so need to avoid type casting there \*/

[ 718](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)#define KB(x) ((x) << 10)

719#else

720#define KB(x) (((size\_t)x) << 10)

721#endif

[ 723](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)#define MB(x) (KB(x) << 10)

[ 725](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)#define GB(x) (MB(x) << 10)

726

[ 728](group__sys-util.md#gaee55275295c076c6d23c994777623253)#define KHZ(x) ((x) \* 1000)

[ 730](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)#define MHZ(x) (KHZ(x) \* 1000)

731

744#if defined(CONFIG\_ARCH\_POSIX)

745#define Z\_SPIN\_DELAY(t) k\_busy\_wait(t)

746#else

747#define Z\_SPIN\_DELAY(t)

748#endif

749

[ 765](group__sys-util.md#ga68eb35df6b4715714312df90209accee)#define WAIT\_FOR(expr, timeout, delay\_stmt) \

766 ({ \

767 uint32\_t \_wf\_cycle\_count = k\_us\_to\_cyc\_ceil32(timeout); \

768 uint32\_t \_wf\_start = k\_cycle\_get\_32(); \

769 while (!(expr) && (\_wf\_cycle\_count > (k\_cycle\_get\_32() - \_wf\_start))) { \

770 delay\_stmt; \

771 Z\_SPIN\_DELAY(10); \

772 } \

773 (expr); \

774 })

775

779

780#endif /\* ZEPHYR\_INCLUDE\_SYS\_UTIL\_H\_ \*/

[aa](asm-macro-32-bit-gnu_8h.md#a8be979fed261ea1fe93f3bf629f3aa9b)

irp nz macro MOVR cc s mov cc s endm endr irp aa

**Definition** asm-macro-32-bit-gnu.h:16

[utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)

char \* utf8\_trunc(char \*utf8\_str)

Properly truncate a NULL-terminated UTF-8 string.

[arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec)

static int64\_t arithmetic\_shift\_right(int64\_t value, uint8\_t shift)

Arithmetic shift right.

**Definition** util.h:423

[hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1)

size\_t hex2bin(const char \*hex, size\_t hexlen, uint8\_t \*buf, size\_t buflen)

Convert a hexadecimal string into a binary array.

[bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e)

static void bytecpy(void \*dst, const void \*src, size\_t size)

byte by byte memcpy.

**Definition** util.h:450

[utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9)

char \* utf8\_lcpy(char \*dst, const char \*src, size\_t n)

Copies a UTF-8 encoded string from src to dst.

[IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)

#define IS\_POWER\_OF\_TWO(x)

Check if a x is a power of two.

**Definition** util\_macro.h:77

[mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743)

static void mem\_xor\_128(uint8\_t dst[16], const uint8\_t src1[16], const uint8\_t src2[16])

XOR 128 bits.

**Definition** util.h:699

[bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591)

static uint8\_t bin2bcd(uint8\_t bin)

Convert a binary value to binary coded decimal (BCD 8421).

**Definition** util.h:545

[mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203)

static void mem\_xor\_32(uint8\_t dst[4], const uint8\_t src1[4], const uint8\_t src2[4])

XOR 32 bits.

**Definition** util.h:687

[byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b)

static void byteswp(void \*a, void \*b, size\_t size)

byte by byte swap.

**Definition** util.h:469

[mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4)

static void mem\_xor\_n(uint8\_t \*dst, const uint8\_t \*src1, const uint8\_t \*src2, size\_t len)

XOR n bytes.

**Definition** util.h:673

[hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c)

int hex2char(uint8\_t x, char \*c)

Convert a single hexadecimal nibble into a character.

[bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4)

static uint8\_t bcd2bin(uint8\_t bcd)

Convert a binary coded decimal (BCD 8421) value to binary.

**Definition** util.h:533

[char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6)

int char2hex(char c, uint8\_t \*x)

Convert a single character into a hexadecimal nibble.

[u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33)

uint8\_t u8\_to\_dec(char \*buf, uint8\_t buflen, uint8\_t value)

Convert a uint8\_t into a decimal string representation.

[is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e)

static bool is\_power\_of\_two(unsigned int x)

Is x a power of two?

**Definition** util.h:411

[bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)

size\_t bin2hex(const uint8\_t \*buf, size\_t buflen, char \*hex, size\_t hexlen)

Convert a binary array into string representation.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

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
