---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/print__format_8h_source.html
original_path: doxygen/html/print__format_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

print\_format.h

[Go to the documentation of this file.](print__format_8h.md)

1/\* Copyright (c) 2023 Google LLC

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

5#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_DSP\_PRINT\_FORMAT\_H

6#define ZEPHYR\_INCLUDE\_ZEPHYR\_DSP\_PRINT\_FORMAT\_H

7

8#include <[inttypes.h](inttypes_8h.md)>

9#include <[stdlib.h](stdlib_8h.md)>

10#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

11

26

[ 30](group__math__printing.md#ga08618ad8449ee21f0a57c151541e8ef8)#define PRIq(precision) "s%" PRIu32 ".%0" STRINGIFY(precision) PRIu32

31

32static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \_\_\_PRIq\_arg\_shift([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) q, int shift)

33{

34 if (shift < 0) {

35 return [llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)(q) >> -shift;

36 } else {

37 return [llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)(q) << shift;

38 }

39}

40

41#define \_\_EXP2(a, b) a ## b

42#define \_\_EXP(a, b) \_\_EXP2(a ## e, b)

43#define \_\_CONSTPOW(C, x) \_\_EXP(C, x)

44

45#define \_\_PRIq\_arg\_shift(q, shift) \_\_\_PRIq\_arg\_shift(q, ((shift) + (8 \* (4 - (int)sizeof(q)))))

46#define \_\_PRIq\_arg\_get(q, shift, h, l) FIELD\_GET(GENMASK64(h, l), \_\_PRIq\_arg\_shift(q, shift))

47#define \_\_PRIq\_arg\_get\_int(q, shift) \_\_PRIq\_arg\_get(q, shift, 63, 31)

48#define \_\_PRIq\_arg\_get\_frac(q, precision, shift) \

49 ((\_\_PRIq\_arg\_get(q, shift, 30, 0) \* \_\_CONSTPOW(1, precision)) / INT32\_MAX)

50

[ 58](group__math__printing.md#gad0393d2bb183784a9c09f2c05d7987f9)#define PRIq\_arg(q, precision, shift) \

59 ((q) < 0 ? "-" : ""), (uint32\_t)\_\_PRIq\_arg\_get\_int(q, shift), \

60 (uint32\_t)\_\_PRIq\_arg\_get\_frac(q, precision, shift)

61

65

66#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_DSP\_PRINT\_FORMAT\_H \*/

[types.h](include_2zephyr_2dsp_2types_8h.md)

[inttypes.h](inttypes_8h.md)

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[stdlib.h](stdlib_8h.md)

[llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)

static long long llabs(long long \_\_n)

**Definition** stdlib.h:70

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [print\_format.h](print__format_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
