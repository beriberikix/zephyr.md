---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2toolchain_2llvm_8h_source.html
original_path: doxygen/html/include_2zephyr_2toolchain_2llvm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llvm.h

[Go to the documentation of this file.](include_2zephyr_2toolchain_2llvm_8h.md)

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

16#ifndef \_\_fallthrough

17#if \_\_clang\_major\_\_ >= 10

18#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

19#endif

20#endif

21

[ 22](include_2zephyr_2toolchain_2llvm_8h.md#acdbda8f5e81a320dfdbc32bda1b33fad)#define TOOLCHAIN\_CLANG\_VERSION \

23 ((\_\_clang\_major\_\_ \* 10000) + (\_\_clang\_minor\_\_ \* 100) + \

24 \_\_clang\_patchlevel\_\_)

25

[ 26](include_2zephyr_2toolchain_2llvm_8h.md#a763b60a74b3b8917b8a91614f1d443e4)#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 1

27

28#if TOOLCHAIN\_CLANG\_VERSION >= 30800

29#define TOOLCHAIN\_HAS\_C\_GENERIC 1

30#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

31#endif

32

33#include <[zephyr/toolchain/gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)>

34

[ 35](include_2zephyr_2toolchain_2llvm_8h.md#a056ed97bac0f04be423885dc21b9df00)#define TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY "-Wsizeof-array-decay"

[ 36](include_2zephyr_2toolchain_2llvm_8h.md#a486884c167e8aa780419637b44ae18e6)#define TOOLCHAIN\_WARNING\_UNNEEDED\_INTERNAL\_DECLARATION "-Wunneeded-internal-declaration"

37

[ 38](include_2zephyr_2toolchain_2llvm_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)#define TOOLCHAIN\_DISABLE\_CLANG\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(clang, warning)

[ 39](include_2zephyr_2toolchain_2llvm_8h.md#a35eaaf7a69eae890687c196e81304667)#define TOOLCHAIN\_ENABLE\_CLANG\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(clang, warning)

40

41/\*

42 \* Provide these definitions only when minimal libc is used.

43 \* Avoid collision with defines from include/zephyr/toolchain/zephyr\_stdint.h

44 \*/

45#ifdef CONFIG\_MINIMAL\_LIBC

46

47/\*

48 \* Predefined \_\_INTN\_C/\_\_UINTN\_C macros are provided by clang starting in version 20.1.

49 \* Avoid redefining these macros if a sufficiently modern clang is being used.

50 \*/

51#if TOOLCHAIN\_CLANG\_VERSION < 200100

52

53#define \_\_int\_c(v, suffix) v ## suffix

54#define int\_c(v, suffix) \_\_int\_c(v, suffix)

55#define uint\_c(v, suffix) \_\_int\_c(v ## U, suffix)

56

57#ifndef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

58

59#ifdef \_\_INT64\_TYPE\_\_

60#undef \_\_int\_least64\_c\_suffix\_\_

61#undef \_\_int\_least32\_c\_suffix\_\_

62#undef \_\_int\_least16\_c\_suffix\_\_

63#undef \_\_int\_least8\_c\_suffix\_\_

64#ifdef \_\_INT64\_C\_SUFFIX\_\_

65#define \_\_int\_least64\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

66#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

67#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

68#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT64\_C\_SUFFIX\_\_

69#endif /\* \_\_INT64\_C\_SUFFIX\_\_ \*/

70#endif /\* \_\_INT64\_TYPE\_\_ \*/

71

72#ifdef \_\_INT\_LEAST64\_TYPE\_\_

73#ifdef \_\_int\_least64\_c\_suffix\_\_

74#define \_\_INT64\_C(x) int\_c(x, \_\_int\_least64\_c\_suffix\_\_)

75#define \_\_UINT64\_C(x) uint\_c(x, \_\_int\_least64\_c\_suffix\_\_)

76#else

77#define \_\_INT64\_C(x) x

78#define \_\_UINT64\_C(x) x ## U

79#endif /\* \_\_int\_least64\_c\_suffix\_\_ \*/

80#endif /\* \_\_INT\_LEAST64\_TYPE\_\_ \*/

81

82#ifdef \_\_INT32\_TYPE\_\_

83#undef \_\_int\_least32\_c\_suffix\_\_

84#undef \_\_int\_least16\_c\_suffix\_\_

85#undef \_\_int\_least8\_c\_suffix\_\_

86#ifdef \_\_INT32\_C\_SUFFIX\_\_

87#define \_\_int\_least32\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

88#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

89#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT32\_C\_SUFFIX\_\_

90#endif /\* \_\_INT32\_C\_SUFFIX\_\_ \*/

91#endif /\* \_\_INT32\_TYPE\_\_ \*/

92

93#ifdef \_\_INT\_LEAST32\_TYPE\_\_

94#ifdef \_\_int\_least32\_c\_suffix\_\_

95#define \_\_INT32\_C(x) int\_c(x, \_\_int\_least32\_c\_suffix\_\_)

96#define \_\_UINT32\_C(x) uint\_c(x, \_\_int\_least32\_c\_suffix\_\_)

97#else

98#define \_\_INT32\_C(x) x

99#define \_\_UINT32\_C(x) x ## U

100#endif /\* \_\_int\_least32\_c\_suffix\_\_ \*/

101#endif /\* \_\_INT\_LEAST32\_TYPE\_\_ \*/

102

103#endif /\* !CONFIG\_ENFORCE\_ZEPHYR\_STDINT \*/

104

105#ifdef \_\_INT16\_TYPE\_\_

106#undef \_\_int\_least16\_c\_suffix\_\_

107#undef \_\_int\_least8\_c\_suffix\_\_

108#ifdef \_\_INT16\_C\_SUFFIX\_\_

109#define \_\_int\_least16\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

110#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT16\_C\_SUFFIX\_\_

111#endif /\* \_\_INT16\_C\_SUFFIX\_\_ \*/

112#endif /\* \_\_INT16\_TYPE\_\_ \*/

113

114#ifdef \_\_INT\_LEAST16\_TYPE\_\_

115#ifdef \_\_int\_least16\_c\_suffix\_\_

116#define \_\_INT16\_C(x) int\_c(x, \_\_int\_least16\_c\_suffix\_\_)

117#define \_\_UINT16\_C(x) uint\_c(x, \_\_int\_least16\_c\_suffix\_\_)

118#else

119#define \_\_INT16\_C(x) x

120#define \_\_UINT16\_C(x) x ## U

121#endif /\* \_\_int\_least16\_c\_suffix\_\_ \*/

122#endif /\* \_\_INT\_LEAST16\_TYPE\_\_ \*/

123

124#ifdef \_\_INT8\_TYPE\_\_

125#undef \_\_int\_least8\_c\_suffix\_\_

126#ifdef \_\_INT8\_C\_SUFFIX\_\_

127#define \_\_int\_least8\_c\_suffix\_\_ \_\_INT8\_C\_SUFFIX\_\_

128#endif /\* \_\_INT8\_C\_SUFFIX\_\_ \*/

129#endif /\* \_\_INT8\_TYPE\_\_ \*/

130

131#ifdef \_\_INT\_LEAST8\_TYPE\_\_

132#ifdef \_\_int\_least8\_c\_suffix\_\_

133#define \_\_INT8\_C(x) int\_c(x, \_\_int\_least8\_c\_suffix\_\_)

134#define \_\_UINT8\_C(x) uint\_c(x, \_\_int\_least8\_c\_suffix\_\_)

135#else

136#define \_\_INT8\_C(x) x

137#define \_\_UINT8\_C(x) x ## U

138#endif /\* \_\_int\_least8\_c\_suffix\_\_ \*/

139#endif /\* \_\_INT\_LEAST8\_TYPE\_\_ \*/

140

141#define \_\_INTMAX\_C(x) int\_c(x, \_\_INTMAX\_C\_SUFFIX\_\_)

142#define \_\_UINTMAX\_C(x) int\_c(x, \_\_UINTMAX\_C\_SUFFIX\_\_)

143

144#endif /\* TOOLCHAIN\_CLANG\_VERSION < 200100 \*/

145

146#endif /\* CONFIG\_MINIMAL\_LIBC \*/

147

148#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_LLVM\_H\_ \*/

[gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)

GCC toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
