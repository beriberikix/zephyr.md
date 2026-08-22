---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2toolchain_2common_8h_source.html
original_path: doxygen/html/include_2zephyr_2toolchain_2common_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h

[Go to the documentation of this file.](include_2zephyr_2toolchain_2common_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2025 Siemens AG

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_

9#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_

10

11#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

12#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

13#endif

14

21

22/\* Abstract use of extern keyword for compatibility between C and C++ \*/

23#ifdef \_\_cplusplus

24#define EXTERN\_C extern "C"

25#else

[ 26](include_2zephyr_2toolchain_2common_8h.md#abbaccfbed35b945162c27ef6d3748e77)#define EXTERN\_C extern

27#endif

28

29/\* Use TASK\_ENTRY\_CPP to tag task entry points defined in C++ files. \*/

30

31#ifdef \_\_cplusplus

32#define TASK\_ENTRY\_CPP extern "C"

33#endif

34

35#ifndef ZRESTRICT

36#ifndef \_\_cplusplus

[ 37](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)#define ZRESTRICT restrict

38#else

39#define ZRESTRICT

40#endif

41#endif

42

43/\*

44 \* Generate a reference to an external symbol.

45 \* The reference indicates to the linker that the symbol is required

46 \* by the module containing the reference and should be included

47 \* in the image if the module is in the image.

48 \*

49 \* The assembler directive ".set" is used to define a local symbol.

50 \* No memory is allocated, and the local symbol does not appear in

51 \* the symbol table.

52 \*/

53

54#ifdef \_ASMLANGUAGE

55 #define REQUIRES(sym) .set sym ## \_Requires, sym

56#else

[ 57](include_2zephyr_2toolchain_2common_8h.md#ab9df20a7e00611b6bdfb246b35a761fc) #define REQUIRES(sym) \_\_asm\_\_ (".set " # sym "\_Requires, " # sym "\n\t");

58#endif

59

60#ifdef \_ASMLANGUAGE

61 #define SECTION .section

62#endif

63

64/\*

65 \* General directive for assembly code, to align the following symbol, in bytes.

66 \*

67 \* Example:

68 \*

69 \* ALIGN(4)

70 \* test\_symbol:

71 \*

72 \* 'test\_symbol' will get aligned to 4 bytes.

73 \*/

74

75#if defined(\_ASMLANGUAGE) && !defined(\_LINKER)

76

77 #if defined(CONFIG\_X86) || defined(CONFIG\_ARM) || defined(CONFIG\_ARM64) || \

78 defined(CONFIG\_RISCV) || defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS) || \

79 defined(CONFIG\_ARCH\_POSIX) || defined(CONFIG\_RX)

80 #define ALIGN(x) .balign x

81 #elif defined(CONFIG\_ARC)

82 /\* .align assembler directive is supported by all ARC toolchains and it is

83 \* implemented in the same way across ARC toolchains.

84 \*/

85 #define ALIGN(x) .align x

86 #elif defined(CONFIG\_SPARC)

87 #define ALIGN(x) .align x

88 #else

89 #error Architecture unsupported

90 #endif

91

92#endif /\* defined(\_ASMLANGUAGE) && !defined(\_LINKER) \*/

93

94/\*

95 \* If the project is being built for speed (i.e. not for minimum size) then

96 \* align functions and branches in executable sections to improve performance.

97 \*/

98

99#ifdef \_ASMLANGUAGE

100

101 #if defined(CONFIG\_X86)

102

103 #ifdef PERF\_OPT

104 #define PERFOPT\_ALIGN .balign 16

105 #else

106 #define PERFOPT\_ALIGN .balign 1

107 #endif

108

109 #elif defined(CONFIG\_ARM) || defined(CONFIG\_ARM64)

110

111 #define PERFOPT\_ALIGN .balign 4

112

113 #elif defined(CONFIG\_ARC)

114

115 /\* .align assembler directive is supposed by all ARC toolchains and it is

116 \* implemented in a same way across ARC toolchains.

117 \*/

118 #define PERFOPT\_ALIGN .align 4

119

120 #elif defined(CONFIG\_RISCV) || defined(CONFIG\_XTENSA) || \

121 defined(CONFIG\_MIPS) || defined(CONFIG\_RX)

122 #define PERFOPT\_ALIGN .balign 4

123

124 #elif defined(CONFIG\_ARCH\_POSIX)

125

126 #elif defined(CONFIG\_SPARC)

127

128 #define PERFOPT\_ALIGN .align 4

129

130 #else

131

132 #error Architecture unsupported

133

134 #endif

135

136 #define GC\_SECTION(sym) SECTION .text.##sym, "ax"

137

138#endif /\* \_ASMLANGUAGE \*/

139

140/\* force inlining a function \*/

141

142#if !defined(\_ASMLANGUAGE)

143 #ifdef CONFIG\_COVERAGE

144 /\*

145 \* The always\_inline attribute forces a function to be inlined,

146 \* even ignoring -fno-inline. So for code coverage, do not

147 \* force inlining of these functions to keep their bodies around

148 \* so their number of executions can be counted.

149 \*

150 \* Note that "inline" is kept here for kobject\_hash.c and

151 \* priv\_stacks\_hash.c. These are built without compiler flags

152 \* used for coverage. ALWAYS\_INLINE cannot be empty as compiler

153 \* would complain about unused functions. Attaching unused

154 \* attribute would result in their text sections balloon more than

155 \* 10 times in size, as those functions are kept in text section.

156 \* So just keep "inline" here.

157 \*/

158 #define ALWAYS\_INLINE inline

159 #else

[ 160](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) #define ALWAYS\_INLINE inline \_\_attribute\_\_((always\_inline))

161 #endif

162#endif

163

164#define Z\_STRINGIFY(x) #x

[ 165](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)#define STRINGIFY(s) Z\_STRINGIFY(s)

166

167/\* concatenate the values of the arguments into one \*/

168#define \_DO\_CONCAT(x, y) x ## y

169#define \_CONCAT(x, y) \_DO\_CONCAT(x, y)

170

171/\* Additionally used as a sentinel by gen\_syscalls.py to identify what

172 \* functions are system calls

173 \*

174 \* Note POSIX unit tests don't still generate the system call stubs, so

175 \* until https://github.com/zephyrproject-rtos/zephyr/issues/5006 is

176 \* fixed via possibly #4174, we introduce this hack -- which will

177 \* disallow us to test system calls in POSIX unit testing (currently

178 \* not used).

179 \*/

180#ifndef ZTEST\_UNITTEST

181#define \_\_syscall static inline

182#define \_\_syscall\_always\_inline static inline \_\_attribute\_\_((always\_inline))

183#else

184#define \_\_syscall

185#define \_\_syscall\_always\_inline

186#endif /\* ZTEST\_UNITTEST \*/

187

188/\* Definitions for struct declaration tags. These are sentinel values used by

189 \* parse\_syscalls.py to gather a list of names of struct declarations that

190 \* have these tags applied for them.

191 \*/

192

193/\* Indicates this is a driver subsystem \*/

194#define \_\_subsystem

195

196/\* Indicates this is a network socket object \*/

197#define \_\_net\_socket

198

199#ifndef BUILD\_ASSERT

200/\* Compile-time assertion that makes the build to fail.

201 \* Common implementation swallows the message.

202 \*/

203#define BUILD\_ASSERT(EXPR, MSG...) \

204 enum \_CONCAT(\_\_build\_assert\_enum, \_\_COUNTER\_\_) { \

205 \_CONCAT(\_\_build\_assert, \_\_COUNTER\_\_) = 1 / !!(EXPR) \

206 }

207#endif

208

209/\*

210 \* This is meant to be used in conjunction with \_\_in\_section() and similar

211 \* where scattered structure instances are concatenated together by the linker

212 \* and walked by the code at run time just like a contiguous array of such

213 \* structures.

214 \*

215 \* Assemblers and linkers may insert alignment padding by default whose

216 \* size is larger than the natural alignment for those structures when

217 \* gathering various section segments together, messing up the array walk.

218 \* To prevent this, we need to provide an explicit alignment not to rely

219 \* on the default that might just work by luck.

220 \*

221 \* Alignment statements in linker scripts are not sufficient as

222 \* the assembler may add padding by itself to each segment when switching

223 \* between sections within the same file even if it merges many such segments

224 \* into a single section in the end.

225 \*/

226#define Z\_DECL\_ALIGN(type) \_\_aligned(\_\_alignof(type)) type

227

228/\* Check if a pointer is aligned for against a specific byte boundary \*/

[ 229](include_2zephyr_2toolchain_2common_8h.md#accd51a2e6e0aacde1d3c7ad7497e40ec)#define IS\_PTR\_ALIGNED\_BYTES(ptr, bytes) ((((uintptr\_t)ptr) % bytes) == 0)

230

231/\* Check if a pointer is aligned enough for a particular data type. \*/

[ 232](include_2zephyr_2toolchain_2common_8h.md#ab13eb1fd10a663089d43679e8c172f71)#define IS\_PTR\_ALIGNED(ptr, type) IS\_PTR\_ALIGNED\_BYTES(ptr, \_\_alignof(type))

233

[ 241](include_2zephyr_2toolchain_2common_8h.md#ad9b02fb67670e2aed5766db629cd4bfa)#define LINKER\_KEEP(symbol) \

242 static const void \* const symbol##\_ptr \_\_used \

243 \_\_attribute\_\_((\_\_section\_\_(".symbol\_to\_keep"))) = (void \*)&symbol

244

245#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [common.h](include_2zephyr_2toolchain_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
