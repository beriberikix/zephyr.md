---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/llvm_8h_source.html
original_path: doxygen/html/llvm_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

33/\*

34 \* Provide these definitions only when minimal libc is used.

35 \* Avoid collision with defines from include/zephyr/toolchain/zephyr\_stdint.h

36 \*/

37#ifdef CONFIG\_MINIMAL\_LIBC

38

39#define \_\_int\_c(v, suffix) v ## suffix

40#define int\_c(v, suffix) \_\_int\_c(v, suffix)

41#define uint\_c(v, suffix) \_\_int\_c(v ## U, suffix)

42

43#ifndef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

44

45#ifdef \_\_INT64\_TYPE\_\_

46#undef \_\_int\_least64\_c\_suffix\_\_

47#undef \_\_int\_least32\_c\_suffix\_\_

48#undef \_\_int\_least16\_c\_suffix\_\_

49#undef \_\_int\_least8\_c\_suffix\_\_

50#ifdef \_\_INT64\_C\_SUFFIX\_\_

51#define \_\_int\_least64\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

52#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

53#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

54#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

55#endif /\* \_\_INT64\_C\_SUFFIX\_\_ \*/

56#endif /\* \_\_INT64\_TYPE\_\_ \*/

57

58#ifdef \_\_INT\_LEAST64\_TYPE\_\_

59#ifdef \_\_int\_least64\_c\_suffix\_\_

60#define \_\_INT64\_C(x) int\_c(x, \_\_int\_least64\_c\_suffix\_\_)

61#define \_\_UINT64\_C(x) uint\_c(x, \_\_int\_least64\_c\_suffix\_\_)

62#else

63#define \_\_INT64\_C(x) x

64#define \_\_UINT64\_C(x) x ## U

65#endif /\* \_\_int\_least64\_c\_suffix\_\_ \*/

66#endif /\* \_\_INT\_LEAST64\_TYPE\_\_ \*/

67

68#ifdef \_\_INT32\_TYPE\_\_

69#undef \_\_int\_least32\_c\_suffix\_\_

70#undef \_\_int\_least16\_c\_suffix\_\_

71#undef \_\_int\_least8\_c\_suffix\_\_

72#ifdef \_\_INT32\_C\_SUFFIX\_\_

73#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

74#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

75#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

76#endif /\* \_\_INT32\_C\_SUFFIX\_\_ \*/

77#endif /\* \_\_INT32\_TYPE\_\_ \*/

78

79#ifdef \_\_INT\_LEAST32\_TYPE\_\_

80#ifdef \_\_int\_least32\_c\_suffix\_\_

81#define \_\_INT32\_C(x) int\_c(x, \_\_int\_least32\_c\_suffix\_\_)

82#define \_\_UINT32\_C(x) uint\_c(x, \_\_int\_least32\_c\_suffix\_\_)

83#else

84#define \_\_INT32\_C(x) x

85#define \_\_UINT32\_C(x) x ## U

86#endif /\* \_\_int\_least32\_c\_suffix\_\_ \*/

87#endif /\* \_\_INT\_LEAST32\_TYPE\_\_ \*/

88

89#endif /\* !CONFIG\_ENFORCE\_ZEPHYR\_STDINT \*/

90

91#ifdef \_\_INT16\_TYPE\_\_

92#undef \_\_int\_least16\_c\_suffix\_\_

93#undef \_\_int\_least8\_c\_suffix\_\_

94#ifdef \_\_INT16\_C\_SUFFIX\_\_

95#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

96#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

97#endif /\* \_\_INT16\_C\_SUFFIX\_\_ \*/

98#endif /\* \_\_INT16\_TYPE\_\_ \*/

99

100#ifdef \_\_INT\_LEAST16\_TYPE\_\_

101#ifdef \_\_int\_least16\_c\_suffix\_\_

102#define \_\_INT16\_C(x) int\_c(x, \_\_int\_least16\_c\_suffix\_\_)

103#define \_\_UINT16\_C(x) uint\_c(x, \_\_int\_least16\_c\_suffix\_\_)

104#else

105#define \_\_INT16\_C(x) x

106#define \_\_UINT16\_C(x) x ## U

107#endif /\* \_\_int\_least16\_c\_suffix\_\_ \*/

108#endif /\* \_\_INT\_LEAST16\_TYPE\_\_ \*/

109

110#ifdef \_\_INT8\_TYPE\_\_

111#undef \_\_int\_least8\_c\_suffix\_\_

112#ifdef \_\_INT8\_C\_SUFFIX\_\_

113#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT8\_C\_SUFFIX\_\_

114#endif /\* \_\_INT8\_C\_SUFFIX\_\_ \*/

115#endif /\* \_\_INT8\_TYPE\_\_ \*/

116

117#ifdef \_\_INT\_LEAST8\_TYPE\_\_

118#ifdef \_\_int\_least8\_c\_suffix\_\_

119#define \_\_INT8\_C(x) int\_c(x, \_\_int\_least8\_c\_suffix\_\_)

120#define \_\_UINT8\_C(x) uint\_c(x, \_\_int\_least8\_c\_suffix\_\_)

121#else

122#define \_\_INT8\_C(x) x

123#define \_\_UINT8\_C(x) x ## U

124#endif /\* \_\_int\_least8\_c\_suffix\_\_ \*/

125#endif /\* \_\_INT\_LEAST8\_TYPE\_\_ \*/

126

127#define \_\_INTMAX\_C(x) int\_c(x, \_\_INTMAX\_C\_SUFFIX\_\_)

128#define \_\_UINTMAX\_C(x) int\_c(x, \_\_UINTMAX\_C\_SUFFIX\_\_)

129

130#endif /\* CONFIG\_MINIMAL\_LIBC \*/

131

132#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_ \*/

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [llvm.h](llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
