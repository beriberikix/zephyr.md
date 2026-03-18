---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/____assert_8h_source.html
original_path: doxygen/html/____assert_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

\_\_assert.h

[Go to the documentation of this file.](____assert_8h.md)

1/\*

2 \* Copyright (c) 2011-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_\_\_ASSERT\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_\_\_ASSERT\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12

13#ifdef CONFIG\_ASSERT

14#ifndef \_\_ASSERT\_ON

15#define \_\_ASSERT\_ON CONFIG\_ASSERT\_LEVEL

16#endif

17#endif

18

19#ifdef CONFIG\_FORCE\_NO\_ASSERT

20#undef \_\_ASSERT\_ON

21#define \_\_ASSERT\_ON 0

22#endif

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\* Wrapper around printk to avoid including printk.h in assert.h \*/

[ 29](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)void \_\_printf\_like(1, 2) [assert\_print](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)(const char \*fmt, ...);

30

31#ifdef \_\_cplusplus

32}

33#endif

34

35#if defined(CONFIG\_ASSERT\_VERBOSE)

36#define \_\_ASSERT\_PRINT(fmt, ...) assert\_print(fmt, ##\_\_VA\_ARGS\_\_)

37#else /\* CONFIG\_ASSERT\_VERBOSE \*/

38#define \_\_ASSERT\_PRINT(fmt, ...)

39#endif /\* CONFIG\_ASSERT\_VERBOSE \*/

40

41#ifdef CONFIG\_ASSERT\_NO\_MSG\_INFO

42#define \_\_ASSERT\_MSG\_INFO(fmt, ...)

43#else /\* CONFIG\_ASSERT\_NO\_MSG\_INFO \*/

44#define \_\_ASSERT\_MSG\_INFO(fmt, ...) \_\_ASSERT\_PRINT("\t" fmt "\n", ##\_\_VA\_ARGS\_\_)

45#endif /\* CONFIG\_ASSERT\_NO\_MSG\_INFO \*/

46

47#if !defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

48#define \_\_ASSERT\_LOC(test) \

49 \_\_ASSERT\_PRINT("ASSERTION FAIL [%s] @ %s:%d\n", \

50 Z\_STRINGIFY(test), \

51 \_\_FILE\_\_, \_\_LINE\_\_)

52#endif

53

54#if defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

55#define \_\_ASSERT\_LOC(test) \

56 \_\_ASSERT\_PRINT("ASSERTION FAIL @ %s:%d\n", \

57 \_\_FILE\_\_, \_\_LINE\_\_)

58#endif

59

60#if !defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

61#define \_\_ASSERT\_LOC(test) \

62 \_\_ASSERT\_PRINT("ASSERTION FAIL [%s]\n", \

63 Z\_STRINGIFY(test))

64#endif

65

66#if defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

67#define \_\_ASSERT\_LOC(test) \

68 \_\_ASSERT\_PRINT("ASSERTION FAIL\n")

69#endif

70

71#ifdef \_\_ASSERT\_ON

72#if (\_\_ASSERT\_ON < 0) || (\_\_ASSERT\_ON > 2)

73#error "Invalid \_\_ASSERT() level: must be between 0 and 2"

74#endif

75

76#if \_\_ASSERT\_ON

77

78#ifdef \_\_cplusplus

79extern "C" {

80#endif

81

82#ifdef CONFIG\_ASSERT\_NO\_FILE\_INFO

83void assert\_post\_action(void);

84#define \_\_ASSERT\_POST\_ACTION() assert\_post\_action()

85#else /\* CONFIG\_ASSERT\_NO\_FILE\_INFO \*/

86void assert\_post\_action(const char \*file, unsigned int line);

87#define \_\_ASSERT\_POST\_ACTION() assert\_post\_action(\_\_FILE\_\_, \_\_LINE\_\_)

88#endif /\* CONFIG\_ASSERT\_NO\_FILE\_INFO \*/

89

90/\*

91 \* When the assert test mode is enabled, the default kernel fatal error handler

92 \* and the custom assert hook function may return in order to allow the test to

93 \* proceed.

94 \*/

95#ifdef CONFIG\_ASSERT\_TEST

96#define \_\_ASSERT\_UNREACHABLE

97#else

98#define \_\_ASSERT\_UNREACHABLE CODE\_UNREACHABLE

99#endif

100

101#ifdef \_\_cplusplus

102}

103#endif

104

105#define \_\_ASSERT\_NO\_MSG(test) \

106 do { \

107 if (!(test)) { \

108 \_\_ASSERT\_LOC(test); \

109 \_\_ASSERT\_POST\_ACTION(); \

110 \_\_ASSERT\_UNREACHABLE; \

111 } \

112 } while (false)

113

114#define \_\_ASSERT(test, fmt, ...) \

115 do { \

116 if (!(test)) { \

117 \_\_ASSERT\_LOC(test); \

118 \_\_ASSERT\_MSG\_INFO(fmt, ##\_\_VA\_ARGS\_\_); \

119 \_\_ASSERT\_POST\_ACTION(); \

120 \_\_ASSERT\_UNREACHABLE; \

121 } \

122 } while (false)

123

124#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) \

125 do { \

126 expr2; \

127 \_\_ASSERT(test, fmt, ##\_\_VA\_ARGS\_\_); \

128 } while (false)

129

130#if (\_\_ASSERT\_ON == 1)

131#warning "\_\_ASSERT() statements are ENABLED"

132#endif

133#else

134#define \_\_ASSERT(test, fmt, ...) { }

135#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) expr1

136#define \_\_ASSERT\_NO\_MSG(test) { }

137#define \_\_ASSERT\_POST\_ACTION() { }

138#endif

139#else

140#define \_\_ASSERT(test, fmt, ...) { }

141#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) expr1

142#define \_\_ASSERT\_NO\_MSG(test) { }

143#define \_\_ASSERT\_POST\_ACTION() { }

144#endif

145

146#endif /\* ZEPHYR\_INCLUDE\_SYS\_\_\_ASSERT\_H\_ \*/

[assert\_print](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)

void assert\_print(const char \*fmt,...)

[stdbool.h](stdbool_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [\_\_assert.h](____assert_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
