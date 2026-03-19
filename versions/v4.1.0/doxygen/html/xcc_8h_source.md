---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xcc_8h_source.html
original_path: doxygen/html/xcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

18#define \_\_deprecated

19

20#define \_\_in\_section\_unique(seg) \

21 \_\_attribute\_\_((section("." STRINGIFY(seg) "." STRINGIFY(\_\_COUNTER\_\_))))

22

23#define \_\_in\_section\_unique\_named(seg, name) \

24 \_\_attribute\_\_((section("." STRINGIFY(seg) \

25 "." STRINGIFY(\_\_COUNTER\_\_) \

26 "." STRINGIFY(name))))

27

28/\* toolchain/gcc.h errors out if \_\_BYTE\_ORDER\_\_ cannot be determined

29 \* there. However, \_\_BYTE\_ORDER\_\_ is actually being defined later in

30 \* this file. So define \_\_BYTE\_ORDER\_\_ to skip the check in gcc.h

31 \* and undefine after including gcc.h.

32 \*

33 \* Clang has it defined so there is no need to work around.

34 \*/

35#ifndef \_\_clang\_\_

36#define \_\_BYTE\_ORDER\_\_

37#endif

38

39#ifdef \_\_clang\_\_

40#include <[zephyr/toolchain/llvm.h](llvm_8h.md)>

41#else

42#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

43#endif

44

45#ifndef \_\_clang\_\_

46#undef \_\_BYTE\_ORDER\_\_

47#endif

48

49#include <[stdbool.h](stdbool_8h.md)>

50

51#ifndef \_\_INT8\_C

52#define \_\_INT8\_C(x) x

53#endif

54

55#ifndef INT8\_C

[ 56](xcc_8h.md#a1eaa7db37089dcdfb60227725c9c1585)#define INT8\_C(x) \_\_INT8\_C(x)

57#endif

58

59#ifndef \_\_UINT8\_C

60#define \_\_UINT8\_C(x) x ## U

61#endif

62

63#ifndef UINT8\_C

[ 64](xcc_8h.md#acd2aa09844a8a245cf7fdbb808e215e5)#define UINT8\_C(x) \_\_UINT8\_C(x)

65#endif

66

67#ifndef \_\_INT16\_C

68#define \_\_INT16\_C(x) x

69#endif

70

71#ifndef INT16\_C

[ 72](xcc_8h.md#a838b261fec725cb0f5d5b6769d3521e7)#define INT16\_C(x) \_\_INT16\_C(x)

73#endif

74

75#ifndef \_\_UINT16\_C

76#define \_\_UINT16\_C(x) x ## U

77#endif

78

79#ifndef UINT16\_C

[ 80](xcc_8h.md#a1cb39a2cfaf899fd38730c7637807708)#define UINT16\_C(x) \_\_UINT16\_C(x)

81#endif

82

83#ifndef \_\_INT32\_C

84#define \_\_INT32\_C(x) x

85#endif

86

87#ifndef INT32\_C

[ 88](xcc_8h.md#ad78650fb7726f4e99205406569ef403d)#define INT32\_C(x) \_\_INT32\_C(x)

89#endif

90

91#ifndef \_\_UINT32\_C

92#define \_\_UINT32\_C(x) x ## U

93#endif

94

95#ifndef UINT32\_C

[ 96](xcc_8h.md#a2451a7ede7ebd810357f1503e9898ea6)#define UINT32\_C(x) \_\_UINT32\_C(x)

97#endif

98

99#ifndef \_\_INT64\_C

100#define \_\_INT64\_C(x) x

101#endif

102

103#ifndef INT64\_C

[ 104](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)#define INT64\_C(x) \_\_INT64\_C(x)

105#endif

106

107#ifndef \_\_UINT64\_C

108#define \_\_UINT64\_C(x) x ## ULL

109#endif

110

111#ifndef UINT64\_C

[ 112](xcc_8h.md#a134ae84400d184ed2570e3270d5472c2)#define UINT64\_C(x) \_\_UINT64\_C(x)

113#endif

114

115#ifndef \_\_INTMAX\_C

116#define \_\_INTMAX\_C(x) x

117#endif

118

119#ifndef INTMAX\_C

[ 120](xcc_8h.md#a846429736de0233f6ecddedb21424ddd)#define INTMAX\_C(x) \_\_INTMAX\_C(x)

121#endif

122

123#ifndef \_\_UINTMAX\_C

124#define \_\_UINTMAX\_C(x) x ## ULL

125#endif

126

127#ifndef UINTMAX\_C

[ 128](xcc_8h.md#ad99c338b32fbeaa158cba21e532dfe5d)#define UINTMAX\_C(x) \_\_UINTMAX\_C(x)

129#endif

130

131#ifndef \_\_COUNTER\_\_

132/\* XCC (GCC-based compiler) doesn't support \_\_COUNTER\_\_

133 \* but this should be good enough

134 \*/

135#define \_\_COUNTER\_\_ \_\_LINE\_\_

136#endif

137

138#ifndef \_\_GCC\_LINKER\_CMD\_\_

139#include <xtensa/config/core.h>

140

141/\*

142 \* XCC does not define the following macros with the expected names, but the

143 \* HAL defines similar ones. Thus we include it and define the missing macros

144 \* ourselves.

145 \*/

146#if XCHAL\_MEMORY\_ORDER == XTHAL\_BIGENDIAN

147#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_BIG\_ENDIAN\_\_

148#elif XCHAL\_MEMORY\_ORDER == XTHAL\_LITTLEENDIAN

149#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_LITTLE\_ENDIAN\_\_

150#else

151#error "Cannot determine \_\_BYTE\_ORDER\_\_"

152#endif

153

154#endif /\* \_\_GCC\_LINKER\_CMD\_\_ \*/

155

156#define \_\_builtin\_unreachable() \_\_builtin\_trap()

157

158/\* Not a full barrier, just a SW barrier \*/

159#define \_\_sync\_synchronize() do { \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); } \

160 while (false)

161

162#endif

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

[llvm.h](llvm_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [xcc.h](xcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
