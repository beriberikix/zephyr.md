---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/xcc_8h_source.html
original_path: doxygen/html/xcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xcc.h

[Go to the documentation of this file.](xcc_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_XCC\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_XCC\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

11#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

12#endif

13

14/\*

15 \* XCC does not support using deprecated attribute in enum,

16 \* so just nullify it here to avoid compilation errors.

17 \*/

18#ifndef \_\_deprecated

19#define \_\_deprecated

20#endif

21

22#define \_\_in\_section\_unique(seg) \

23 \_\_attribute\_\_((section("." STRINGIFY(seg) "." STRINGIFY(\_\_COUNTER\_\_))))

24

25#define \_\_in\_section\_unique\_named(seg, name) \

26 \_\_attribute\_\_((section("." STRINGIFY(seg) \

27 "." STRINGIFY(\_\_COUNTER\_\_) \

28 "." STRINGIFY(name))))

29

30/\* toolchain/gcc.h errors out if \_\_BYTE\_ORDER\_\_ cannot be determined

31 \* there. However, \_\_BYTE\_ORDER\_\_ is actually being defined later in

32 \* this file. So define \_\_BYTE\_ORDER\_\_ to skip the check in gcc.h

33 \* and undefine after including gcc.h.

34 \*

35 \* Clang has it defined so there is no need to work around.

36 \*/

37#ifndef \_\_clang\_\_

38#define \_\_BYTE\_ORDER\_\_

39#endif

40

41#ifdef \_\_clang\_\_

42#include <[zephyr/toolchain/llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)>

43#else

44#include <[zephyr/toolchain/gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)>

45#endif

46

47#ifdef \_\_clang\_\_

48/\* For some reasons, xt-clang does not like "%hhd" or "%hd" (for example)

49 \* being fed int data (same goes for unsigned ones) and will always complain

50 \* about mismatched types. GCC and newer LLVM/Clang do not complain.

51 \* This could be due to xt-clang being based on older LLVM/Clang.

52 \* So skip the check.

53 \*/

54#ifdef \_\_printf\_like

55#undef \_\_printf\_like

56#define \_\_printf\_like(f, a)

57#endif

58#endif

59

60#ifndef \_\_clang\_\_

61#undef \_\_BYTE\_ORDER\_\_

62#endif

63

64#include <[stdbool.h](stdbool_8h.md)>

65

66#ifndef \_\_INT8\_C

67#define \_\_INT8\_C(x) x

68#endif

69

70#ifndef INT8\_C

[ 71](xcc_8h.md#a1eaa7db37089dcdfb60227725c9c1585)#define INT8\_C(x) \_\_INT8\_C(x)

72#endif

73

74#ifndef \_\_UINT8\_C

75#define \_\_UINT8\_C(x) x ## U

76#endif

77

78#ifndef UINT8\_C

[ 79](xcc_8h.md#acd2aa09844a8a245cf7fdbb808e215e5)#define UINT8\_C(x) \_\_UINT8\_C(x)

80#endif

81

82#ifndef \_\_INT16\_C

83#define \_\_INT16\_C(x) x

84#endif

85

86#ifndef INT16\_C

[ 87](xcc_8h.md#a838b261fec725cb0f5d5b6769d3521e7)#define INT16\_C(x) \_\_INT16\_C(x)

88#endif

89

90#ifndef \_\_UINT16\_C

91#define \_\_UINT16\_C(x) x ## U

92#endif

93

94#ifndef UINT16\_C

[ 95](xcc_8h.md#a1cb39a2cfaf899fd38730c7637807708)#define UINT16\_C(x) \_\_UINT16\_C(x)

96#endif

97

98#ifndef \_\_INT32\_C

99#define \_\_INT32\_C(x) x

100#endif

101

102#ifndef INT32\_C

[ 103](xcc_8h.md#ad78650fb7726f4e99205406569ef403d)#define INT32\_C(x) \_\_INT32\_C(x)

104#endif

105

106#ifndef \_\_UINT32\_C

107#define \_\_UINT32\_C(x) x ## U

108#endif

109

110#ifndef UINT32\_C

[ 111](xcc_8h.md#a2451a7ede7ebd810357f1503e9898ea6)#define UINT32\_C(x) \_\_UINT32\_C(x)

112#endif

113

114#ifndef \_\_INT64\_C

115#define \_\_INT64\_C(x) x

116#endif

117

118#ifndef INT64\_C

[ 119](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)#define INT64\_C(x) \_\_INT64\_C(x)

120#endif

121

122#ifndef \_\_UINT64\_C

123#define \_\_UINT64\_C(x) x ## ULL

124#endif

125

126#ifndef UINT64\_C

[ 127](xcc_8h.md#a134ae84400d184ed2570e3270d5472c2)#define UINT64\_C(x) \_\_UINT64\_C(x)

128#endif

129

130#ifndef \_\_INTMAX\_C

131#define \_\_INTMAX\_C(x) x

132#endif

133

134#ifndef INTMAX\_C

[ 135](xcc_8h.md#a846429736de0233f6ecddedb21424ddd)#define INTMAX\_C(x) \_\_INTMAX\_C(x)

136#endif

137

138#ifndef \_\_UINTMAX\_C

139#define \_\_UINTMAX\_C(x) x ## ULL

140#endif

141

142#ifndef UINTMAX\_C

[ 143](xcc_8h.md#ad99c338b32fbeaa158cba21e532dfe5d)#define UINTMAX\_C(x) \_\_UINTMAX\_C(x)

144#endif

145

146#ifndef \_\_COUNTER\_\_

147/\* XCC (GCC-based compiler) doesn't support \_\_COUNTER\_\_

148 \* but this should be good enough

149 \*/

150#define \_\_COUNTER\_\_ \_\_LINE\_\_

151#endif

152

153#ifndef \_\_GCC\_LINKER\_CMD\_\_

154#include <xtensa/config/core.h>

155

156/\*

157 \* XCC does not define the following macros with the expected names, but the

158 \* HAL defines similar ones. Thus we include it and define the missing macros

159 \* ourselves.

160 \*/

161#if XCHAL\_MEMORY\_ORDER == XTHAL\_BIGENDIAN

162#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_BIG\_ENDIAN\_\_

163#elif XCHAL\_MEMORY\_ORDER == XTHAL\_LITTLEENDIAN

164#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_LITTLE\_ENDIAN\_\_

165#else

166#error "Cannot determine \_\_BYTE\_ORDER\_\_"

167#endif

168

169#endif /\* \_\_GCC\_LINKER\_CMD\_\_ \*/

170

171#define \_\_builtin\_unreachable() \_\_builtin\_trap()

172

173/\* Not a full barrier, just a SW barrier \*/

174#define \_\_sync\_synchronize() do { \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); } \

175 while (false)

176

177#endif

[gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)

GCC toolchain abstraction.

[llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [xcc.h](xcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
