---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/include_2zephyr_2toolchain_2common_8h_source.html
original_path: doxygen/html/include_2zephyr_2toolchain_2common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h

[Go to the documentation of this file.](include_2zephyr_2toolchain_2common_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

11#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

12#endif

13

20

21/\* Abstract use of extern keyword for compatibility between C and C++ \*/

22#ifdef \_\_cplusplus

23#define EXTERN\_C extern "C"

24#else

[ 25](include_2zephyr_2toolchain_2common_8h.md#abbaccfbed35b945162c27ef6d3748e77)#define EXTERN\_C extern

26#endif

27

28/\* Use TASK\_ENTRY\_CPP to tag task entry points defined in C++ files. \*/

29

30#ifdef \_\_cplusplus

31#define TASK\_ENTRY\_CPP extern "C"

32#endif

33

34#ifndef ZRESTRICT

35#ifndef \_\_cplusplus

[ 36](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)#define ZRESTRICT restrict

37#else

38#define ZRESTRICT

39#endif

40#endif

41

42/\*

43 \* Generate a reference to an external symbol.

44 \* The reference indicates to the linker that the symbol is required

45 \* by the module containing the reference and should be included

46 \* in the image if the module is in the image.

47 \*

48 \* The assembler directive ".set" is used to define a local symbol.

49 \* No memory is allocated, and the local symbol does not appear in

50 \* the symbol table.

51 \*/

52

53#ifdef \_ASMLANGUAGE

54 #define REQUIRES(sym) .set sym ## \_Requires, sym

55#else

[ 56](include_2zephyr_2toolchain_2common_8h.md#ab9df20a7e00611b6bdfb246b35a761fc) #define REQUIRES(sym) \_\_asm\_\_ (".set " # sym "\_Requires, " # sym "\n\t");

57#endif

58

59#ifdef \_ASMLANGUAGE

60 #define SECTION .section

61#endif

62

63/\*

64 \* If the project is being built for speed (i.e. not for minimum size) then

65 \* align functions and branches in executable sections to improve performance.

66 \*/

67

68#ifdef \_ASMLANGUAGE

69

70 #if defined(CONFIG\_X86)

71

72 #ifdef PERF\_OPT

73 #define PERFOPT\_ALIGN .balign 16

74 #else

75 #define PERFOPT\_ALIGN .balign 1

76 #endif

77

78 #elif defined(CONFIG\_ARM) || defined(CONFIG\_ARM64)

79

80 #define PERFOPT\_ALIGN .balign 4

81

82 #elif defined(CONFIG\_ARC)

83

84 /\* .align assembler directive is supposed by all ARC toolchains and it is

85 \* implemented in a same way across ARC toolchains.

86 \*/

87 #define PERFOPT\_ALIGN .align 4

88

89 #elif defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) || \

90 defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS)

91 #define PERFOPT\_ALIGN .balign 4

92

93 #elif defined(CONFIG\_ARCH\_POSIX)

94

95 #elif defined(CONFIG\_SPARC)

96

97 #define PERFOPT\_ALIGN .align 4

98

99 #else

100

101 #error Architecture unsupported

102

103 #endif

104

105 #define GC\_SECTION(sym) SECTION .text.##sym, "ax"

106

107#endif /\* \_ASMLANGUAGE \*/

108

109/\* force inlining a function \*/

110

111#if !defined(\_ASMLANGUAGE)

112 #ifdef CONFIG\_COVERAGE

113 /\*

114 \* The always\_inline attribute forces a function to be inlined,

115 \* even ignoring -fno-inline. So for code coverage, do not

116 \* force inlining of these functions to keep their bodies around

117 \* so their number of executions can be counted.

118 \*

119 \* Note that "inline" is kept here for kobject\_hash.c and

120 \* priv\_stacks\_hash.c. These are built without compiler flags

121 \* used for coverage. ALWAYS\_INLINE cannot be empty as compiler

122 \* would complain about unused functions. Attaching unused

123 \* attribute would result in their text sections balloon more than

124 \* 10 times in size, as those functions are kept in text section.

125 \* So just keep "inline" here.

126 \*/

127 #define ALWAYS\_INLINE inline

128 #else

[ 129](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) #define ALWAYS\_INLINE inline \_\_attribute\_\_((always\_inline))

130 #endif

131#endif

132

133#define Z\_STRINGIFY(x) #x

[ 134](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)#define STRINGIFY(s) Z\_STRINGIFY(s)

135

136/\* concatenate the values of the arguments into one \*/

137#define \_DO\_CONCAT(x, y) x ## y

138#define \_CONCAT(x, y) \_DO\_CONCAT(x, y)

139

140/\* Additionally used as a sentinel by gen\_syscalls.py to identify what

141 \* functions are system calls

142 \*

143 \* Note POSIX unit tests don't still generate the system call stubs, so

144 \* until https://github.com/zephyrproject-rtos/zephyr/issues/5006 is

145 \* fixed via possibly #4174, we introduce this hack -- which will

146 \* disallow us to test system calls in POSIX unit testing (currently

147 \* not used).

148 \*/

149#ifndef ZTEST\_UNITTEST

150#define \_\_syscall static inline

151#define \_\_syscall\_always\_inline static inline \_\_attribute\_\_((always\_inline))

152#else

153#define \_\_syscall

154#define \_\_syscall\_always\_inline

155#endif /\* ZTEST\_UNITTEST \*/

156

157/\* Definitions for struct declaration tags. These are sentinel values used by

158 \* parse\_syscalls.py to gather a list of names of struct declarations that

159 \* have these tags applied for them.

160 \*/

161

162/\* Indicates this is a driver subsystem \*/

163#define \_\_subsystem

164

165/\* Indicates this is a network socket object \*/

166#define \_\_net\_socket

167

168#ifndef BUILD\_ASSERT

169/\* Compile-time assertion that makes the build to fail.

170 \* Common implementation swallows the message.

171 \*/

172#define BUILD\_ASSERT(EXPR, MSG...) \

173 enum \_CONCAT(\_\_build\_assert\_enum, \_\_COUNTER\_\_) { \

174 \_CONCAT(\_\_build\_assert, \_\_COUNTER\_\_) = 1 / !!(EXPR) \

175 }

176#endif

177

178/\*

179 \* This is meant to be used in conjunction with \_\_in\_section() and similar

180 \* where scattered structure instances are concatenated together by the linker

181 \* and walked by the code at run time just like a contiguous array of such

182 \* structures.

183 \*

184 \* Assemblers and linkers may insert alignment padding by default whose

185 \* size is larger than the natural alignment for those structures when

186 \* gathering various section segments together, messing up the array walk.

187 \* To prevent this, we need to provide an explicit alignment not to rely

188 \* on the default that might just work by luck.

189 \*

190 \* Alignment statements in linker scripts are not sufficient as

191 \* the assembler may add padding by itself to each segment when switching

192 \* between sections within the same file even if it merges many such segments

193 \* into a single section in the end.

194 \*/

195#define Z\_DECL\_ALIGN(type) \_\_aligned(\_\_alignof(type)) type

196

197/\* Check if a pointer is aligned for against a specific byte boundary \*/

[ 198](include_2zephyr_2toolchain_2common_8h.md#accd51a2e6e0aacde1d3c7ad7497e40ec)#define IS\_PTR\_ALIGNED\_BYTES(ptr, bytes) ((((uintptr\_t)ptr) % bytes) == 0)

199

200/\* Check if a pointer is aligned enough for a particular data type. \*/

[ 201](include_2zephyr_2toolchain_2common_8h.md#ab13eb1fd10a663089d43679e8c172f71)#define IS\_PTR\_ALIGNED(ptr, type) IS\_PTR\_ALIGNED\_BYTES(ptr, \_\_alignof(type))

202

[ 210](include_2zephyr_2toolchain_2common_8h.md#ad9b02fb67670e2aed5766db629cd4bfa)#define LINKER\_KEEP(symbol) \

211 static const void \* const symbol##\_ptr \_\_used \

212 \_\_attribute\_\_((\_\_section\_\_(".symbol\_to\_keep"))) = (void \*)&symbol

213

214#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [common.h](include_2zephyr_2toolchain_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
