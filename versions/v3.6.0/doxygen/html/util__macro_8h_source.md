---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/util__macro_8h_source.html
original_path: doxygen/html/util__macro_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util\_macro.h

[Go to the documentation of this file.](util__macro_8h.md)

1/\*

2 \* Copyright (c) 2011-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef ZEPHYR\_INCLUDE\_SYS\_UTIL\_MACROS\_H\_

18#define ZEPHYR\_INCLUDE\_SYS\_UTIL\_MACROS\_H\_

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

28

29/\*

30 \* Most of the eldritch implementation details for all the macrobatics

31 \* below (APIs like IS\_ENABLED(), COND\_CODE\_1(), etc.) are hidden away

32 \* in this file.

33 \*/

34#include <[zephyr/sys/util\_internal.h](util__internal_8h.md)>

35

36#ifndef BIT

37#if defined(\_ASMLANGUAGE)

38#define BIT(n) (1 << (n))

39#else

[ 44](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)#define BIT(n) (1UL << (n))

45#endif

46#endif

47

[ 49](group__sys-util.md#gacfdade52af3ced2d87472cec47d14a76)#define BIT64(\_n) (1ULL << (\_n))

50

[ 61](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)#define WRITE\_BIT(var, bit, set) \

62 ((var) = (set) ? ((var) | BIT(bit)) : ((var) & ~BIT(bit)))

63

[ 68](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)#define BIT\_MASK(n) (BIT(n) - 1UL)

69

[ 74](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)#define BIT64\_MASK(n) (BIT64(n) - 1ULL)

75

[ 77](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)#define IS\_POWER\_OF\_TWO(x) (((x) != 0U) && (((x) & ((x) - 1U)) == 0U))

78

[ 87](group__sys-util.md#ga406b5955c2803cdd9d9f19c90f242662)#define IS\_SHIFTED\_BIT\_MASK(m, s) (!(((m) >> (s)) & (((m) >> (s)) + 1U)))

88

[ 94](group__sys-util.md#ga6d4b02e5da10bf93c4697dd6bf239ffd)#define IS\_BIT\_MASK(m) IS\_SHIFTED\_BIT\_MASK(m, 0)

95

[ 124](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)#define IS\_ENABLED(config\_macro) Z\_IS\_ENABLED1(config\_macro)

125/\* INTERNAL: the first pass above is just to expand any existing

126 \* macros, we need the macro value to be e.g. a literal "1" at

127 \* expansion time in the next macro, not "(1)", etc... Standard

128 \* recursive expansion does not work.

129 \*/

130

[ 179](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code) \

180 Z\_COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

181

[ 195](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)#define COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code) \

196 Z\_COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)

197

[ 223](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)#define IF\_ENABLED(\_flag, \_code) \

224 COND\_CODE\_1(\_flag, \_code, ())

225

[ 247](group__sys-util.md#gaa65e031f24a2c0fb4eae240e2c60b36a)#define IF\_DISABLED(\_flag, \_code) \

248 COND\_CODE\_1(\_flag, (), \_code)

249

[ 277](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)#define IS\_EMPTY(...) Z\_IS\_EMPTY\_(\_\_VA\_ARGS\_\_)

278

[ 286](group__sys-util.md#gaa35a6894bca38a8ffb558c2c22a1eee1)#define IS\_EQ(a, b) Z\_IS\_EQ(a, b)

287

[ 315](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)#define LIST\_DROP\_EMPTY(...) \

316 Z\_LIST\_DROP\_FIRST(FOR\_EACH(Z\_LIST\_NO\_EMPTIES, (), \_\_VA\_ARGS\_\_))

317

[ 335](group__sys-util.md#ga2b7cf2a3641be7b89138615764d60ba3)#define EMPTY

336

[ 345](group__sys-util.md#gaaed493c6115c04272077a0f3854b9a83)#define IDENTITY(V) V

346

[ 355](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)#define GET\_ARG\_N(N, ...) Z\_GET\_ARG\_##N(\_\_VA\_ARGS\_\_)

356

[ 365](group__sys-util.md#ga01e1dc9b92e5be6895528d1da5f0c88b)#define GET\_ARGS\_LESS\_N(N, ...) Z\_GET\_ARGS\_LESS\_##N(\_\_VA\_ARGS\_\_)

366

[ 378](group__sys-util.md#ga50cfdf948906976562c3f0625c84c2b2)#define UTIL\_OR(a, b) COND\_CODE\_1(UTIL\_BOOL(a), (a), (b))

379

[ 391](group__sys-util.md#ga26179b776b4a03143e8be1612ef6d853)#define UTIL\_AND(a, b) COND\_CODE\_1(UTIL\_BOOL(a), (b), (0))

392

[ 399](group__sys-util.md#ga90a54212306c3e210ac87fd0bd7b32da)#define UTIL\_INC(x) UTIL\_PRIMITIVE\_CAT(Z\_UTIL\_INC\_, x)

400

[ 407](group__sys-util.md#gaa7623e1e33316024217094698e4d8258)#define UTIL\_DEC(x) UTIL\_PRIMITIVE\_CAT(Z\_UTIL\_DEC\_, x)

408

[ 413](group__sys-util.md#gab23deac75762adfb6bdde2c15d51f158)#define UTIL\_X2(y) UTIL\_PRIMITIVE\_CAT(Z\_UTIL\_X2\_, y)

414

415

[ 442](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)#define LISTIFY(LEN, F, sep, ...) UTIL\_CAT(Z\_UTIL\_LISTIFY\_, LEN)(F, sep, \_\_VA\_ARGS\_\_)

443

[ 465](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)#define FOR\_EACH(F, sep, ...) \

466 Z\_FOR\_EACH(F, sep, REVERSE\_ARGS(\_\_VA\_ARGS\_\_))

467

[ 520](group__sys-util.md#ga24b3862161d725f5503b1bb08f4e339f)#define FOR\_EACH\_NONEMPTY\_TERM(F, term, ...) \

521 COND\_CODE\_0( \

522 /\* are there zero non-empty arguments ? \*/ \

523 NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

524 /\* if so, expand to nothing \*/ \

525 (), \

526 /\* otherwise, expand to: \*/ \

527 (/\* FOR\_EACH() on nonempty elements, \*/ \

528 FOR\_EACH(F, term, LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_)) \

529 /\* plus a final terminator \*/ \

530 \_\_DEBRACKET term \

531 ))

532

[ 557](group__sys-util.md#ga069f709e18eeafb8d276b5ff4fc09d31)#define FOR\_EACH\_IDX(F, sep, ...) \

558 Z\_FOR\_EACH\_IDX(F, sep, REVERSE\_ARGS(\_\_VA\_ARGS\_\_))

559

[ 585](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)#define FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg, ...) \

586 Z\_FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg, REVERSE\_ARGS(\_\_VA\_ARGS\_\_))

587

[ 613](group__sys-util.md#ga2ab7377f5493123ffd29ebd1286457a9)#define FOR\_EACH\_IDX\_FIXED\_ARG(F, sep, fixed\_arg, ...) \

614 Z\_FOR\_EACH\_IDX\_FIXED\_ARG(F, sep, fixed\_arg, REVERSE\_ARGS(\_\_VA\_ARGS\_\_))

615

[ 620](group__sys-util.md#ga58de032c2ed7b4094c447c512dfd3784)#define REVERSE\_ARGS(...) \

621 Z\_FOR\_EACH\_ENGINE(Z\_FOR\_EACH\_EXEC, (,), Z\_BYPASS, \_, \_\_VA\_ARGS\_\_)

622

[ 629](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)#define NUM\_VA\_ARGS\_LESS\_1(...) \

630 NUM\_VA\_ARGS\_LESS\_1\_IMPL(\_\_VA\_ARGS\_\_, 63, 62, 61, \

631 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, \

632 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, \

633 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, \

634 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, \

635 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, \

636 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, ~)

637

[ 658](group__sys-util.md#gaf82371bd6bf317add5276fc6cbd66662)#define MACRO\_MAP\_CAT(...) MACRO\_MAP\_CAT\_(\_\_VA\_ARGS\_\_)

659

[ 673](group__sys-util.md#ga58eba1f911e21da46b8beea264934d55)#define MACRO\_MAP\_CAT\_N(N, ...) MACRO\_MAP\_CAT\_N\_(N, \_\_VA\_ARGS\_\_)

674

678

679#ifdef \_\_cplusplus

680}

681#endif

682

683#endif /\* ZEPHYR\_INCLUDE\_SYS\_UTIL\_MACROS\_H\_ \*/

[util\_internal.h](util__internal_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util\_macro.h](util__macro_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
