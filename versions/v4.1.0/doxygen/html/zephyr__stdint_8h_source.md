---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zephyr__stdint_8h_source.html
original_path: doxygen/html/zephyr__stdint_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

19/\*

20 \* If the compiler does not define \_\_SIZEOF\_INT\_\_ deduce it from \_\_INT\_MAX\_\_

21 \* or INT\_MAX.

22 \*/

23#if !defined(\_\_SIZEOF\_INT\_\_)

24

25#if defined(\_\_INT\_MAX\_\_)

26/\* GCC >= 3.3.0 has \_\_<val>\_\_ implicitly defined. \*/

27#define \_\_Z\_INT\_MAX \_\_INT\_MAX\_\_

28#else

29/\* Fall back to POSIX versions from <limits.h> \*/

30#define \_\_Z\_INT\_MAX INT\_MAX

31#include <[limits.h](limits_8h.md)>

32#endif

33

34#if \_\_Z\_INT\_MAX == 0x7fff

35#define \_\_SIZEOF\_INT\_\_ 2

36#elif \_\_Z\_INT\_MAX == 0x7fffffffL

37#define \_\_SIZEOF\_INT\_\_ 4

38#elif \_\_Z\_INT\_MAX > 0x7fffffffL

39#define \_\_SIZEOF\_INT\_\_ 8

40#endif

41

42#undef \_\_Z\_INT\_MAX

43

44#endif

45

46#if \_\_SIZEOF\_INT\_\_ != 4

47#error "unexpected int width"

48#endif

49

50#undef \_\_INT32\_TYPE\_\_

51#undef \_\_UINT32\_TYPE\_\_

52#undef \_\_INT\_FAST32\_TYPE\_\_

53#undef \_\_UINT\_FAST32\_TYPE\_\_

54#undef \_\_INT\_LEAST32\_TYPE\_\_

55#undef \_\_UINT\_LEAST32\_TYPE\_\_

56#undef \_\_INT64\_TYPE\_\_

57#undef \_\_UINT64\_TYPE\_\_

58#undef \_\_INT\_FAST64\_TYPE\_\_

59#undef \_\_UINT\_FAST64\_TYPE\_\_

60#undef \_\_INT\_LEAST64\_TYPE\_\_

61#undef \_\_UINT\_LEAST64\_TYPE\_\_

62

63#define \_\_INT32\_TYPE\_\_ int

64#define \_\_UINT32\_TYPE\_\_ unsigned int

65#define \_\_INT\_FAST32\_TYPE\_\_ \_\_INT32\_TYPE\_\_

66#define \_\_UINT\_FAST32\_TYPE\_\_ \_\_UINT32\_TYPE\_\_

67#define \_\_INT\_LEAST32\_TYPE\_\_ \_\_INT32\_TYPE\_\_

68#define \_\_UINT\_LEAST32\_TYPE\_\_ \_\_UINT32\_TYPE\_\_

69#define \_\_INT64\_TYPE\_\_ long long int

70#define \_\_UINT64\_TYPE\_\_ unsigned long long int

71#define \_\_INT\_FAST64\_TYPE\_\_ \_\_INT64\_TYPE\_\_

72#define \_\_UINT\_FAST64\_TYPE\_\_ \_\_UINT64\_TYPE\_\_

73#define \_\_INT\_LEAST64\_TYPE\_\_ \_\_INT64\_TYPE\_\_

74#define \_\_UINT\_LEAST64\_TYPE\_\_ \_\_UINT64\_TYPE\_\_

75

76/\*

77 \* The confusion also exists with \_\_INTPTR\_TYPE\_\_ which is either an int

78 \* (even when \_\_INT32\_TYPE\_\_ is a long int) or a long int. Let's redefine

79 \* it to a long int to get some uniformity. Doing so also makes it compatible

80 \* with LP64 (64-bit) targets where a long is always 64-bit wide.

81 \*/

82

83#if \_\_SIZEOF\_POINTER\_\_ != \_\_SIZEOF\_LONG\_\_

84#error "unexpected size difference between pointers and long ints"

85#endif

86

87#undef \_\_INTPTR\_TYPE\_\_

88#undef \_\_UINTPTR\_TYPE\_\_

89#define \_\_INTPTR\_TYPE\_\_ long int

90#define \_\_UINTPTR\_TYPE\_\_ long unsigned int

91

92/\*

93 \* Re-define the INTN\_C(value) integer constant expression macros to match the

94 \* integer types re-defined above.

95 \*/

96

97#undef \_\_INT32\_C

98#undef \_\_UINT32\_C

99#undef \_\_INT64\_C

100#undef \_\_UINT64\_C

101#define \_\_INT32\_C(c) c

102#define \_\_UINT32\_C(c) c ## U

103#define \_\_INT64\_C(c) c ## LL

104#define \_\_UINT64\_C(c) c ## ULL

105

106#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_STDINT\_H\_ \*/

[limits.h](limits_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [zephyr\_stdint.h](zephyr__stdint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
