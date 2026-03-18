---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/xcc_8h_source.html
original_path: doxygen/html/xcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

14/\* toolchain/gcc.h errors out if \_\_BYTE\_ORDER\_\_ cannot be determined

15 \* there. However, \_\_BYTE\_ORDER\_\_ is actually being defined later in

16 \* this file. So define \_\_BYTE\_ORDER\_\_ to skip the check in gcc.h

17 \* and undefine after including gcc.h.

18 \*

19 \* Clang has it defined so there is no need to work around.

20 \*/

21#ifndef \_\_clang\_\_

22#define \_\_BYTE\_ORDER\_\_

23#endif

24

25#ifdef \_\_clang\_\_

26#include <[zephyr/toolchain/llvm.h](llvm_8h.md)>

27#else

28#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

29#endif

30

31#ifndef \_\_clang\_\_

32#undef \_\_BYTE\_ORDER\_\_

33#endif

34

35#include <[stdbool.h](stdbool_8h.md)>

36

37#ifndef \_\_INT8\_C

38#define \_\_INT8\_C(x) x

39#endif

40

41#ifndef INT8\_C

[ 42](xcc_8h.md#a1eaa7db37089dcdfb60227725c9c1585)#define INT8\_C(x) \_\_INT8\_C(x)

43#endif

44

45#ifndef \_\_UINT8\_C

46#define \_\_UINT8\_C(x) x ## U

47#endif

48

49#ifndef UINT8\_C

[ 50](xcc_8h.md#acd2aa09844a8a245cf7fdbb808e215e5)#define UINT8\_C(x) \_\_UINT8\_C(x)

51#endif

52

53#ifndef \_\_INT16\_C

54#define \_\_INT16\_C(x) x

55#endif

56

57#ifndef INT16\_C

[ 58](xcc_8h.md#a838b261fec725cb0f5d5b6769d3521e7)#define INT16\_C(x) \_\_INT16\_C(x)

59#endif

60

61#ifndef \_\_UINT16\_C

62#define \_\_UINT16\_C(x) x ## U

63#endif

64

65#ifndef UINT16\_C

[ 66](xcc_8h.md#a1cb39a2cfaf899fd38730c7637807708)#define UINT16\_C(x) \_\_UINT16\_C(x)

67#endif

68

69#ifndef \_\_INT32\_C

70#define \_\_INT32\_C(x) x

71#endif

72

73#ifndef INT32\_C

[ 74](xcc_8h.md#ad78650fb7726f4e99205406569ef403d)#define INT32\_C(x) \_\_INT32\_C(x)

75#endif

76

77#ifndef \_\_UINT32\_C

78#define \_\_UINT32\_C(x) x ## U

79#endif

80

81#ifndef UINT32\_C

[ 82](xcc_8h.md#a2451a7ede7ebd810357f1503e9898ea6)#define UINT32\_C(x) \_\_UINT32\_C(x)

83#endif

84

85#ifndef \_\_INT64\_C

86#define \_\_INT64\_C(x) x

87#endif

88

89#ifndef INT64\_C

[ 90](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)#define INT64\_C(x) \_\_INT64\_C(x)

91#endif

92

93#ifndef \_\_UINT64\_C

94#define \_\_UINT64\_C(x) x ## ULL

95#endif

96

97#ifndef UINT64\_C

[ 98](xcc_8h.md#a134ae84400d184ed2570e3270d5472c2)#define UINT64\_C(x) \_\_UINT64\_C(x)

99#endif

100

101#ifndef \_\_INTMAX\_C

102#define \_\_INTMAX\_C(x) x

103#endif

104

105#ifndef INTMAX\_C

[ 106](xcc_8h.md#a846429736de0233f6ecddedb21424ddd)#define INTMAX\_C(x) \_\_INTMAX\_C(x)

107#endif

108

109#ifndef \_\_UINTMAX\_C

110#define \_\_UINTMAX\_C(x) x ## ULL

111#endif

112

113#ifndef UINTMAX\_C

[ 114](xcc_8h.md#ad99c338b32fbeaa158cba21e532dfe5d)#define UINTMAX\_C(x) \_\_UINTMAX\_C(x)

115#endif

116

117#ifndef \_\_COUNTER\_\_

118/\* XCC (GCC-based compiler) doesn't support \_\_COUNTER\_\_

119 \* but this should be good enough

120 \*/

121#define \_\_COUNTER\_\_ \_\_LINE\_\_

122#endif

123

124#undef \_\_in\_section\_unique

125#define \_\_in\_section\_unique(seg) \

126 \_\_attribute\_\_((section("." STRINGIFY(seg) "." STRINGIFY(\_\_COUNTER\_\_))))

127

128#undef \_\_in\_section\_unique\_named

129#define \_\_in\_section\_unique\_named(seg, name) \

130 \_\_attribute\_\_((section("." STRINGIFY(seg) \

131 "." STRINGIFY(\_\_COUNTER\_\_) \

132 "." STRINGIFY(name))))

133

134#ifndef \_\_GCC\_LINKER\_CMD\_\_

135#include <xtensa/config/core.h>

136

137/\*

138 \* XCC does not define the following macros with the expected names, but the

139 \* HAL defines similar ones. Thus we include it and define the missing macros

140 \* ourselves.

141 \*/

142#if XCHAL\_MEMORY\_ORDER == XTHAL\_BIGENDIAN

143#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_BIG\_ENDIAN\_\_

144#elif XCHAL\_MEMORY\_ORDER == XTHAL\_LITTLEENDIAN

145#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_LITTLE\_ENDIAN\_\_

146#else

147#error "Cannot determine \_\_BYTE\_ORDER\_\_"

148#endif

149

150#endif /\* \_\_GCC\_LINKER\_CMD\_\_ \*/

151

152#define \_\_builtin\_unreachable() \_\_builtin\_trap()

153

154/\* Not a full barrier, just a SW barrier \*/

155#define \_\_sync\_synchronize() do { \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); } \

156 while (false)

157

158#ifdef \_\_deprecated

159/\*

160 \* XCC does not support using deprecated attribute in enum,

161 \* so just nullify it here to avoid compilation errors.

162 \*/

163#undef \_\_deprecated

164#define \_\_deprecated

165#endif

166

167#endif

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

[llvm.h](llvm_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [xcc.h](xcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
