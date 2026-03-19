---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/____assert_8h_source.html
original_path: doxygen/html/____assert_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

15#ifdef CONFIG\_ASSERT\_LEVEL

16#define \_\_ASSERT\_ON CONFIG\_ASSERT\_LEVEL

17#endif

18#endif

19#endif

20

21#ifdef CONFIG\_FORCE\_NO\_ASSERT

22#undef \_\_ASSERT\_ON

23#define \_\_ASSERT\_ON 0

24#endif

25

26#ifndef \_\_ASSERT\_ON

27#define \_\_ASSERT\_ON 0

28#endif

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\* Wrapper around printk to avoid including printk.h in assert.h \*/

[ 35](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)void \_\_printf\_like(1, 2) [assert\_print](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)(const char \*fmt, ...);

36

37#ifdef \_\_cplusplus

38}

39#endif

40

41#if defined(CONFIG\_ASSERT\_VERBOSE)

42#define \_\_ASSERT\_PRINT(fmt, ...) assert\_print(fmt, ##\_\_VA\_ARGS\_\_)

43#else /\* CONFIG\_ASSERT\_VERBOSE \*/

44#define \_\_ASSERT\_PRINT(fmt, ...)

45#endif /\* CONFIG\_ASSERT\_VERBOSE \*/

46

47#ifdef CONFIG\_ASSERT\_NO\_MSG\_INFO

48#define \_\_ASSERT\_MSG\_INFO(fmt, ...)

49#else /\* CONFIG\_ASSERT\_NO\_MSG\_INFO \*/

50#define \_\_ASSERT\_MSG\_INFO(fmt, ...) \_\_ASSERT\_PRINT("\t" fmt "\n", ##\_\_VA\_ARGS\_\_)

51#endif /\* CONFIG\_ASSERT\_NO\_MSG\_INFO \*/

52

53#if !defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

54#define \_\_ASSERT\_LOC(test) \

55 \_\_ASSERT\_PRINT("ASSERTION FAIL [%s] @ %s:%d\n", \

56 Z\_STRINGIFY(test), \

57 \_\_FILE\_\_, \_\_LINE\_\_)

58#endif

59

60#if defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && !defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

61#define \_\_ASSERT\_LOC(test) \

62 \_\_ASSERT\_PRINT("ASSERTION FAIL @ %s:%d\n", \

63 \_\_FILE\_\_, \_\_LINE\_\_)

64#endif

65

66#if !defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

67#define \_\_ASSERT\_LOC(test) \

68 \_\_ASSERT\_PRINT("ASSERTION FAIL [%s]\n", \

69 Z\_STRINGIFY(test))

70#endif

71

72#if defined(CONFIG\_ASSERT\_NO\_COND\_INFO) && defined(CONFIG\_ASSERT\_NO\_FILE\_INFO)

73#define \_\_ASSERT\_LOC(test) \

74 \_\_ASSERT\_PRINT("ASSERTION FAIL\n")

75#endif

76

77#ifdef \_\_ASSERT\_ON

78#if (\_\_ASSERT\_ON < 0) || (\_\_ASSERT\_ON > 2)

79#error "Invalid \_\_ASSERT() level: must be between 0 and 2"

80#endif

81

82#if \_\_ASSERT\_ON

83

84#ifdef \_\_cplusplus

85extern "C" {

86#endif

87

88#ifdef CONFIG\_ASSERT\_NO\_FILE\_INFO

89void assert\_post\_action(void);

90#define \_\_ASSERT\_POST\_ACTION() assert\_post\_action()

91#else /\* CONFIG\_ASSERT\_NO\_FILE\_INFO \*/

92void assert\_post\_action(const char \*file, unsigned int line);

93#define \_\_ASSERT\_POST\_ACTION() assert\_post\_action(\_\_FILE\_\_, \_\_LINE\_\_)

94#endif /\* CONFIG\_ASSERT\_NO\_FILE\_INFO \*/

95

96/\*

97 \* When the assert test mode is enabled, the default kernel fatal error handler

98 \* and the custom assert hook function may return in order to allow the test to

99 \* proceed.

100 \*/

101#ifdef CONFIG\_ASSERT\_TEST

102#define \_\_ASSERT\_UNREACHABLE

103#else

104#define \_\_ASSERT\_UNREACHABLE CODE\_UNREACHABLE

105#endif

106

107#ifdef \_\_cplusplus

108}

109#endif

110

111#define \_\_ASSERT\_NO\_MSG(test) \

112 do { \

113 if (!(test)) { \

114 \_\_ASSERT\_LOC(test); \

115 \_\_ASSERT\_POST\_ACTION(); \

116 \_\_ASSERT\_UNREACHABLE; \

117 } \

118 } while (false)

119

120#define \_\_ASSERT(test, fmt, ...) \

121 do { \

122 if (!(test)) { \

123 \_\_ASSERT\_LOC(test); \

124 \_\_ASSERT\_MSG\_INFO(fmt, ##\_\_VA\_ARGS\_\_); \

125 \_\_ASSERT\_POST\_ACTION(); \

126 \_\_ASSERT\_UNREACHABLE; \

127 } \

128 } while (false)

129

130#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) \

131 do { \

132 expr2; \

133 \_\_ASSERT(test, fmt, ##\_\_VA\_ARGS\_\_); \

134 } while (false)

135

136#if (\_\_ASSERT\_ON == 1)

137#warning "\_\_ASSERT() statements are ENABLED"

138#endif

139#else

140#define \_\_ASSERT(test, fmt, ...) { }

141#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) expr1

142#define \_\_ASSERT\_NO\_MSG(test) { }

143#define \_\_ASSERT\_POST\_ACTION() { }

144#endif

145#else

146#define \_\_ASSERT(test, fmt, ...) { }

147#define \_\_ASSERT\_EVAL(expr1, expr2, test, fmt, ...) expr1

148#define \_\_ASSERT\_NO\_MSG(test) { }

149#define \_\_ASSERT\_POST\_ACTION() { }

150#endif

151

152#endif /\* ZEPHYR\_INCLUDE\_SYS\_\_\_ASSERT\_H\_ \*/

[assert\_print](____assert_8h.md#a156598a0c2fc4b91756d41ab0f8fd563)

void assert\_print(const char \*fmt,...)

[stdbool.h](stdbool_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [\_\_assert.h](____assert_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
