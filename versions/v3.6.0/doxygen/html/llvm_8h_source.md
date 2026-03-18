---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/llvm_8h_source.html
original_path: doxygen/html/llvm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llvm.h

[Go to the documentation of this file.](llvm_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

11#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

12#endif

13

14#define \_\_no\_optimization \_\_attribute\_\_((optnone))

15

16#if \_\_clang\_major\_\_ >= 10

17#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

18#endif

19

[ 20](llvm_8h.md#acdbda8f5e81a320dfdbc32bda1b33fad)#define TOOLCHAIN\_CLANG\_VERSION \

21 ((\_\_clang\_major\_\_ \* 10000) + (\_\_clang\_minor\_\_ \* 100) + \

22 \_\_clang\_patchlevel\_\_)

23

[ 24](llvm_8h.md#a763b60a74b3b8917b8a91614f1d443e4)#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 1

25

26#if TOOLCHAIN\_CLANG\_VERSION >= 30800

27#define TOOLCHAIN\_HAS\_C\_GENERIC 1

28#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

29#endif

30

31#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

32

33#ifndef \_\_INT8\_C

34#define \_\_INT8\_C(x) x

35#endif

36

37#ifndef INT8\_C

[ 38](llvm_8h.md#a1eaa7db37089dcdfb60227725c9c1585)#define INT8\_C(x) \_\_INT8\_C(x)

39#endif

40

41#ifndef \_\_UINT8\_C

42#define \_\_UINT8\_C(x) x ## U

43#endif

44

45#ifndef UINT8\_C

[ 46](llvm_8h.md#acd2aa09844a8a245cf7fdbb808e215e5)#define UINT8\_C(x) \_\_UINT8\_C(x)

47#endif

48

49#ifndef \_\_INT16\_C

50#define \_\_INT16\_C(x) x

51#endif

52

53#ifndef INT16\_C

[ 54](llvm_8h.md#a838b261fec725cb0f5d5b6769d3521e7)#define INT16\_C(x) \_\_INT16\_C(x)

55#endif

56

57#ifndef \_\_UINT16\_C

58#define \_\_UINT16\_C(x) x ## U

59#endif

60

61#ifndef UINT16\_C

[ 62](llvm_8h.md#a1cb39a2cfaf899fd38730c7637807708)#define UINT16\_C(x) \_\_UINT16\_C(x)

63#endif

64

65#ifndef \_\_INT32\_C

66#define \_\_INT32\_C(x) x

67#endif

68

69#ifndef INT32\_C

[ 70](llvm_8h.md#ad78650fb7726f4e99205406569ef403d)#define INT32\_C(x) \_\_INT32\_C(x)

71#endif

72

73#ifndef \_\_UINT32\_C

74#define \_\_UINT32\_C(x) x ## U

75#endif

76

77#ifndef UINT32\_C

[ 78](llvm_8h.md#a2451a7ede7ebd810357f1503e9898ea6)#define UINT32\_C(x) \_\_UINT32\_C(x)

79#endif

80

81#ifndef \_\_INT64\_C

82#define \_\_INT64\_C(x) x

83#endif

84

85#ifndef INT64\_C

[ 86](llvm_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)#define INT64\_C(x) \_\_INT64\_C(x)

87#endif

88

89#ifndef \_\_UINT64\_C

90#define \_\_UINT64\_C(x) x ## ULL

91#endif

92

93#ifndef UINT64\_C

[ 94](llvm_8h.md#a134ae84400d184ed2570e3270d5472c2)#define UINT64\_C(x) \_\_UINT64\_C(x)

95#endif

96

97#ifndef \_\_INTMAX\_C

98#define \_\_INTMAX\_C(x) x

99#endif

100

101#ifndef INTMAX\_C

[ 102](llvm_8h.md#a846429736de0233f6ecddedb21424ddd)#define INTMAX\_C(x) \_\_INTMAX\_C(x)

103#endif

104

105#ifndef \_\_UINTMAX\_C

106#define \_\_UINTMAX\_C(x) x ## ULL

107#endif

108

109#ifndef UINTMAX\_C

[ 110](llvm_8h.md#ad99c338b32fbeaa158cba21e532dfe5d)#define UINTMAX\_C(x) \_\_UINTMAX\_C(x)

111#endif

112

113#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_ \*/

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [llvm.h](llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
