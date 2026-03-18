---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/zephyr__stdint_8h_source.html
original_path: doxygen/html/zephyr__stdint_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zephyr\_stdint.h

[Go to the documentation of this file.](zephyr__stdint_8h.md)

1/\*

2 \* Copyright (c) 2019 BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_STDINT\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_STDINT\_H\_

9

10/\*

11 \* Some gcc versions and/or configurations as found in the Zephyr SDK

12 \* (questionably) define \_\_INT32\_TYPE\_\_ and derivatives as a long int

13 \* which makes the printf format checker to complain about long vs int

14 \* mismatch when %u is given a uint32\_t argument, and uint32\_t pointers not

15 \* being compatible with int pointers. Let's redefine them to follow

16 \* common expectations and usage.

17 \*/

18

19#if \_\_SIZEOF\_INT\_\_ != 4

20#error "unexpected int width"

21#endif

22

23#undef \_\_INT32\_TYPE\_\_

24#undef \_\_UINT32\_TYPE\_\_

25#undef \_\_INT\_FAST32\_TYPE\_\_

26#undef \_\_UINT\_FAST32\_TYPE\_\_

27#undef \_\_INT\_LEAST32\_TYPE\_\_

28#undef \_\_UINT\_LEAST32\_TYPE\_\_

29#undef \_\_INT64\_TYPE\_\_

30#undef \_\_UINT64\_TYPE\_\_

31#undef \_\_INT\_FAST64\_TYPE\_\_

32#undef \_\_UINT\_FAST64\_TYPE\_\_

33#undef \_\_INT\_LEAST64\_TYPE\_\_

34#undef \_\_UINT\_LEAST64\_TYPE\_\_

35

36#define \_\_INT32\_TYPE\_\_ int

37#define \_\_UINT32\_TYPE\_\_ unsigned int

38#define \_\_INT\_FAST32\_TYPE\_\_ \_\_INT32\_TYPE\_\_

39#define \_\_UINT\_FAST32\_TYPE\_\_ \_\_UINT32\_TYPE\_\_

40#define \_\_INT\_LEAST32\_TYPE\_\_ \_\_INT32\_TYPE\_\_

41#define \_\_UINT\_LEAST32\_TYPE\_\_ \_\_UINT32\_TYPE\_\_

42#define \_\_INT64\_TYPE\_\_ long long int

43#define \_\_UINT64\_TYPE\_\_ unsigned long long int

44#define \_\_INT\_FAST64\_TYPE\_\_ \_\_INT64\_TYPE\_\_

45#define \_\_UINT\_FAST64\_TYPE\_\_ \_\_UINT64\_TYPE\_\_

46#define \_\_INT\_LEAST64\_TYPE\_\_ \_\_INT64\_TYPE\_\_

47#define \_\_UINT\_LEAST64\_TYPE\_\_ \_\_UINT64\_TYPE\_\_

48

49/\*

50 \* The confusion also exists with \_\_INTPTR\_TYPE\_\_ which is either an int

51 \* (even when \_\_INT32\_TYPE\_\_ is a long int) or a long int. Let's redefine

52 \* it to a long int to get some uniformity. Doing so also makes it compatible

53 \* with LP64 (64-bit) targets where a long is always 64-bit wide.

54 \*/

55

56#if \_\_SIZEOF\_POINTER\_\_ != \_\_SIZEOF\_LONG\_\_

57#error "unexpected size difference between pointers and long ints"

58#endif

59

60#undef \_\_INTPTR\_TYPE\_\_

61#undef \_\_UINTPTR\_TYPE\_\_

62#define \_\_INTPTR\_TYPE\_\_ long int

63#define \_\_UINTPTR\_TYPE\_\_ long unsigned int

64

65/\*

66 \* Re-define the INTN\_C(value) integer constant expression macros to match the

67 \* integer types re-defined above.

68 \*/

69

70#undef \_\_INT32\_C

71#undef \_\_UINT32\_C

72#undef \_\_INT64\_C

73#undef \_\_UINT64\_C

74#define \_\_INT32\_C(c) c

75#define \_\_UINT32\_C(c) c ## U

76#define \_\_INT64\_C(c) c ## LL

77#define \_\_UINT64\_C(c) c ## ULL

78

79#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_STDINT\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [zephyr\_stdint.h](zephyr__stdint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
