---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/interpolation_8h_source.html
original_path: doxygen/html/interpolation_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

interpolation.h

[Go to the documentation of this file.](interpolation_8h.md)

1/\*

2 \* Copyright (c) 2024 Embeint Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_MATH\_INTERPOLATION\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_MATH\_INTERPOLATION\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[math.h](math_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

21

[ 37](interpolation_8h.md#a8abbb1799796222b39a051819bd19a2a)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [linear\_interpolate](interpolation_8h.md#a8abbb1799796222b39a051819bd19a2a)(const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*x\_axis, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*y\_axis, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len,

38 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) x)

39{

40 float rise, run, slope;

41 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) x\_shifted;

42 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx\_low = 0;

43

44 /\* Handle out of bounds values \*/

45 if (x <= x\_axis[0]) {

46 return y\_axis[0];

47 } else if (x >= x\_axis[len - 1]) {

48 return y\_axis[len - 1];

49 }

50

51 /\* Find the lower x axis bucket \*/

52 while (x >= x\_axis[idx\_low + 1]) {

53 idx\_low++;

54 }

55

56 /\* Shift input to origin \*/

57 x\_shifted = x - x\_axis[idx\_low];

58 if (x\_shifted == 0) {

59 return y\_axis[idx\_low];

60 }

61

62 /\* Local slope \*/

63 rise = y\_axis[idx\_low + 1] - y\_axis[idx\_low];

64 run = x\_axis[idx\_low + 1] - x\_axis[idx\_low];

65 slope = rise / run;

66

67 /\* Apply slope, undo origin shift and round \*/

68 return roundf(y\_axis[idx\_low] + (slope \* x\_shifted));

69}

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_MATH\_INTERPOLATION\_H\_ \*/

[linear\_interpolate](interpolation_8h.md#a8abbb1799796222b39a051819bd19a2a)

static int32\_t linear\_interpolate(const int32\_t \*x\_axis, const int32\_t \*y\_axis, uint8\_t len, int32\_t x)

Perform a linear interpolation across an arbitrary curve.

**Definition** interpolation.h:37

[math.h](math_8h.md)

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [math](dir_76cc2d861a01f89f8d0ad119e28af149.md)
- [interpolation.h](interpolation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
