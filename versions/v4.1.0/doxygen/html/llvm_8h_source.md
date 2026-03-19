---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/llvm_8h_source.html
original_path: doxygen/html/llvm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 33](llvm_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)#define TOOLCHAIN\_DISABLE\_CLANG\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(clang, warning)

[ 34](llvm_8h.md#a35eaaf7a69eae890687c196e81304667)#define TOOLCHAIN\_ENABLE\_CLANG\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(clang, warning)

35

36/\*

37 \* Provide these definitions only when minimal libc is used.

38 \* Avoid collision with defines from include/zephyr/toolchain/zephyr\_stdint.h

39 \*/

40#ifdef CONFIG\_MINIMAL\_LIBC

41

42#define \_\_int\_c(v, suffix) v ## suffix

43#define int\_c(v, suffix) \_\_int\_c(v, suffix)

44#define uint\_c(v, suffix) \_\_int\_c(v ## U, suffix)

45

46#ifndef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

47

48#ifdef \_\_INT64\_TYPE\_\_

49#undef \_\_int\_least64\_c\_suffix\_\_

50#undef \_\_int\_least32\_c\_suffix\_\_

51#undef \_\_int\_least16\_c\_suffix\_\_

52#undef \_\_int\_least8\_c\_suffix\_\_

53#ifdef \_\_INT64\_C\_SUFFIX\_\_

54#define \_\_int\_least64\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

55#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

56#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

57#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

58#endif /\* \_\_INT64\_C\_SUFFIX\_\_ \*/

59#endif /\* \_\_INT64\_TYPE\_\_ \*/

60

61#ifdef \_\_INT\_LEAST64\_TYPE\_\_

62#ifdef \_\_int\_least64\_c\_suffix\_\_

63#define \_\_INT64\_C(x) int\_c(x, \_\_int\_least64\_c\_suffix\_\_)

64#define \_\_UINT64\_C(x) uint\_c(x, \_\_int\_least64\_c\_suffix\_\_)

65#else

66#define \_\_INT64\_C(x) x

67#define \_\_UINT64\_C(x) x ## U

68#endif /\* \_\_int\_least64\_c\_suffix\_\_ \*/

69#endif /\* \_\_INT\_LEAST64\_TYPE\_\_ \*/

70

71#ifdef \_\_INT32\_TYPE\_\_

72#undef \_\_int\_least32\_c\_suffix\_\_

73#undef \_\_int\_least16\_c\_suffix\_\_

74#undef \_\_int\_least8\_c\_suffix\_\_

75#ifdef \_\_INT32\_C\_SUFFIX\_\_

76#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

77#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

78#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

79#endif /\* \_\_INT32\_C\_SUFFIX\_\_ \*/

80#endif /\* \_\_INT32\_TYPE\_\_ \*/

81

82#ifdef \_\_INT\_LEAST32\_TYPE\_\_

83#ifdef \_\_int\_least32\_c\_suffix\_\_

84#define \_\_INT32\_C(x) int\_c(x, \_\_int\_least32\_c\_suffix\_\_)

85#define \_\_UINT32\_C(x) uint\_c(x, \_\_int\_least32\_c\_suffix\_\_)

86#else

87#define \_\_INT32\_C(x) x

88#define \_\_UINT32\_C(x) x ## U

89#endif /\* \_\_int\_least32\_c\_suffix\_\_ \*/

90#endif /\* \_\_INT\_LEAST32\_TYPE\_\_ \*/

91

92#endif /\* !CONFIG\_ENFORCE\_ZEPHYR\_STDINT \*/

93

94#ifdef \_\_INT16\_TYPE\_\_

95#undef \_\_int\_least16\_c\_suffix\_\_

96#undef \_\_int\_least8\_c\_suffix\_\_

97#ifdef \_\_INT16\_C\_SUFFIX\_\_

98#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

99#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

100#endif /\* \_\_INT16\_C\_SUFFIX\_\_ \*/

101#endif /\* \_\_INT16\_TYPE\_\_ \*/

102

103#ifdef \_\_INT\_LEAST16\_TYPE\_\_

104#ifdef \_\_int\_least16\_c\_suffix\_\_

105#define \_\_INT16\_C(x) int\_c(x, \_\_int\_least16\_c\_suffix\_\_)

106#define \_\_UINT16\_C(x) uint\_c(x, \_\_int\_least16\_c\_suffix\_\_)

107#else

108#define \_\_INT16\_C(x) x

109#define \_\_UINT16\_C(x) x ## U

110#endif /\* \_\_int\_least16\_c\_suffix\_\_ \*/

111#endif /\* \_\_INT\_LEAST16\_TYPE\_\_ \*/

112

113#ifdef \_\_INT8\_TYPE\_\_

114#undef \_\_int\_least8\_c\_suffix\_\_

115#ifdef \_\_INT8\_C\_SUFFIX\_\_

116#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT8\_C\_SUFFIX\_\_

117#endif /\* \_\_INT8\_C\_SUFFIX\_\_ \*/

118#endif /\* \_\_INT8\_TYPE\_\_ \*/

119

120#ifdef \_\_INT\_LEAST8\_TYPE\_\_

121#ifdef \_\_int\_least8\_c\_suffix\_\_

122#define \_\_INT8\_C(x) int\_c(x, \_\_int\_least8\_c\_suffix\_\_)

123#define \_\_UINT8\_C(x) uint\_c(x, \_\_int\_least8\_c\_suffix\_\_)

124#else

125#define \_\_INT8\_C(x) x

126#define \_\_UINT8\_C(x) x ## U

127#endif /\* \_\_int\_least8\_c\_suffix\_\_ \*/

128#endif /\* \_\_INT\_LEAST8\_TYPE\_\_ \*/

129

130#define \_\_INTMAX\_C(x) int\_c(x, \_\_INTMAX\_C\_SUFFIX\_\_)

131#define \_\_UINTMAX\_C(x) int\_c(x, \_\_UINTMAX\_C\_SUFFIX\_\_)

132

133#endif /\* CONFIG\_MINIMAL\_LIBC \*/

134

135#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_ \*/

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [llvm.h](llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
