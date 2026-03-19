---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/limits_8h_source.html
original_path: doxygen/html/limits_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

limits.h

[Go to the documentation of this file.](limits_8h.md)

1/\* limits.h \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_LIMITS\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_LIMITS\_H\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16#if \_\_CHAR\_BIT\_\_ == 8

17#define UCHAR\_MAX 0xFFU

18#else

19#error "unexpected \_\_CHAR\_BIT\_\_ value"

20#endif

21

[ 22](limits_8h.md#a8c13fdd8c2840edf0cb04a65297037bb)#define SCHAR\_MAX \_\_SCHAR\_MAX\_\_

[ 23](limits_8h.md#aa05d197000ad5c143ada0fcd9379b236)#define SCHAR\_MIN (-SCHAR\_MAX - 1)

24

25#ifdef \_\_CHAR\_UNSIGNED\_\_

26 /\* 'char' is an unsigned type \*/

27 #define CHAR\_MAX UCHAR\_MAX

28 #define CHAR\_MIN 0

29#else

30 /\* 'char' is a signed type \*/

[ 31](limits_8h.md#a778eefd6535a9d4b752fca5dd0af58db) #define CHAR\_MAX SCHAR\_MAX

[ 32](limits_8h.md#a5d707bd32338557ced18c6ac76ca1b3a) #define CHAR\_MIN SCHAR\_MIN

33#endif

34

[ 35](limits_8h.md#a308d9dd2c0028ddb184b455bbd7865de)#define CHAR\_BIT \_\_CHAR\_BIT\_\_

[ 36](limits_8h.md#a88c78a5170af546a3417d28875fd3710)#define LONG\_BIT (\_\_SIZEOF\_LONG\_\_ \* CHAR\_BIT)

[ 37](limits_8h.md#af95e2cdeed2bb68c59e2c3d07b6c3d04)#define WORD\_BIT (\_\_SIZEOF\_POINTER\_\_ \* CHAR\_BIT)

38

[ 39](limits_8h.md#a9ec306f36d50c7375e74f0d1c55a3a67)#define INT\_MAX \_\_INT\_MAX\_\_

[ 40](limits_8h.md#a1f758438cb1c7bcf55da2431f5e319e6)#define SHRT\_MAX \_\_SHRT\_MAX\_\_

[ 41](limits_8h.md#a50fece4db74f09568b2938db583c5655)#define LONG\_MAX \_\_LONG\_MAX\_\_

[ 42](limits_8h.md#a23ec2cf7fc07ea8f817bbac758402baf)#define LLONG\_MAX \_\_LONG\_LONG\_MAX\_\_

43

[ 44](limits_8h.md#a21658776274b3d146c674318b635a334)#define INT\_MIN (-INT\_MAX - 1)

[ 45](limits_8h.md#ae59de266aceffa1c258ac13f45fe0d18)#define SHRT\_MIN (-SHRT\_MAX - 1)

[ 46](limits_8h.md#ae8a44c5a7436466221e0f3859d02420f)#define LONG\_MIN (-LONG\_MAX - 1L)

[ 47](limits_8h.md#af17a13b2ae0e9c24c020ac1f044f30c2)#define LLONG\_MIN (-LLONG\_MAX - 1LL)

48

49#if \_\_SIZE\_MAX\_\_ == \_\_UINT32\_MAX\_\_

[ 50](limits_8h.md#a2d6569aa794c2f23e90691e60d2f3ad2)#define SSIZE\_MAX \_\_INT32\_MAX\_\_

51#elif \_\_SIZE\_MAX\_\_ == \_\_UINT64\_MAX\_\_

52#define SSIZE\_MAX \_\_INT64\_MAX\_\_

53#else

54#error "unexpected \_\_SIZE\_MAX\_\_ value"

55#endif

56

57#if \_\_SIZEOF\_SHORT\_\_ == 2

58#define USHRT\_MAX 0xFFFFU

59#else

60#error "unexpected \_\_SIZEOF\_SHORT\_\_ value"

61#endif

62

63#if \_\_SIZEOF\_INT\_\_ == 4

64#define UINT\_MAX 0xFFFFFFFFU

65#else

66#error "unexpected \_\_SIZEOF\_INT\_\_ value"

67#endif

68

69#if \_\_SIZEOF\_LONG\_\_ == 4

70#define ULONG\_MAX 0xFFFFFFFFUL

71#elif \_\_SIZEOF\_LONG\_\_ == 8

72#define ULONG\_MAX 0xFFFFFFFFFFFFFFFFUL

73#else

74#error "unexpected \_\_SIZEOF\_LONG\_\_ value"

75#endif

76

77#if \_\_SIZEOF\_LONG\_LONG\_\_ == 8

78#define ULLONG\_MAX 0xFFFFFFFFFFFFFFFFULL

79#else

80#error "unexpected \_\_SIZEOF\_LONG\_LONG\_\_ value"

81#endif

82

[ 83](limits_8h.md#ae688d728e1acdfe5988c7db45d6f0166)#define PATH\_MAX 256

84

85#ifdef \_\_cplusplus

86}

87#endif

88

89#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_LIMITS\_H\_ \*/

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [limits.h](limits_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
