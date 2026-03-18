---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mwdt_8h_source.html
original_path: doxygen/html/mwdt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mwdt.h

[Go to the documentation of this file.](mwdt_8h.md)

1/\*

2 \* Copyright (c) 2020 Synopsys.

3 \* Author: Eugeniy Paltsev <Eugeniy.Paltsev@synopsys.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_MWDT\_H\_

9#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_MWDT\_H\_

10

11#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

12#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

13#endif

14

15#ifndef \_LINKER

16#if defined(\_ASMLANGUAGE)

17

18#include <[zephyr/toolchain/common.h](common_8h.md)>

19

20#define FUNC\_CODE()

21#define FUNC\_INSTR(a)

22

23#ifdef \_\_MW\_ASM\_RV\_MACRO\_\_

24.macro section\_var\_mwdt, section, symbol

25 .section \section().\symbol, "aw"

26 \symbol :

27.endm

28

29.macro section\_func\_mwdt, section, symbol

30 .section \section().\symbol, "ax"

31 FUNC\_CODE()

32 PERFOPT\_ALIGN

33 \symbol :

34 FUNC\_INSTR(symbol)

35.endm

36

37.macro section\_subsec\_func\_mwdt, section, subsection, symbol

38 .section \section().\subsection, "ax"

39 PERFOPT\_ALIGN

40 \symbol :

41.endm

42#else

43.macro section\_var\_mwdt, section, symbol

44 .section .\&section\&.\&symbol, "aw"

45 symbol :

46.endm

47

48.macro section\_func\_mwdt, section, symbol

49 .section .\&section\&.\&symbol, "ax"

50 FUNC\_CODE()

51 PERFOPT\_ALIGN

52 symbol :

53 FUNC\_INSTR(symbol)

54.endm

55

56.macro section\_subsec\_func\_mwdt, section, subsection, symbol

57 .section .\&section\&.\&subsection, "ax"

58 PERFOPT\_ALIGN

59 symbol :

60.endm

61#endif /\* \_\_MW\_ASM\_RV\_MACRO\_\_ \*/

62

63#define SECTION\_VAR(sect, sym) section\_var\_mwdt sect, sym

64#define SECTION\_FUNC(sect, sym) section\_func\_mwdt sect, sym

65#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

66 section\_subsec\_func\_mwdt sect, subsec, sym

67

68#ifdef \_\_MW\_ASM\_RV\_MACRO\_\_

69.macro glbl\_text\_mwdt, symbol

70 .globl \symbol

71 .type \symbol, @function

72.endm

73

74.macro glbl\_data\_mwdt, symbol

75 .globl \symbol

76 .type \symbol, @object

77.endm

78

79.macro weak\_data\_mwdt, symbol

80 .weak \symbol

81 .type \symbol, @object

82.endm

83

84.macro weak\_text\_mwdt, symbol

85 .weak \symbol

86 .type \symbol, @function

87.endm

88#else

89.macro glbl\_text\_mwdt, symbol

90 .globl symbol

91 .type symbol, @function

92.endm

93

94.macro glbl\_data\_mwdt, symbol

95 .globl symbol

96 .type symbol, @object

97.endm

98

99.macro weak\_data\_mwdt, symbol

100 .weak symbol

101 .type symbol, @object

102.endm

103

104.macro weak\_text\_mwdt, symbol

105 .weak symbol

106 .type symbol, @function

107.endm

108#endif /\* \_\_MW\_ASM\_RV\_MACRO\_\_ \*/

109

110#define GTEXT(sym) glbl\_text\_mwdt sym

111#define GDATA(sym) glbl\_data\_mwdt sym

112#define WDATA(sym) weak\_data\_mwdt sym

113#define WTEXT(sym) weak\_text\_mwdt sym

114

115#else /\* defined(\_ASMLANGUAGE) \*/

116

117/\* MWDT toolchain misses ssize\_t definition which is used by Zephyr \*/

118#ifndef \_SSIZE\_T\_DEFINED

119#define \_SSIZE\_T\_DEFINED

120#ifdef CONFIG\_64BIT

121 typedef long [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

122#else

123 typedef int [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

124#endif

125#endif /\* \_SSIZE\_T\_DEFINED \*/

126

127#ifdef CONFIG\_NEWLIB\_LIBC

128 #error "ARC MWDT doesn't support building with CONFIG\_NEWLIB\_LIBC as it doesn't have newlib"

129#endif /\* CONFIG\_NEWLIB\_LIBC \*/

130

131#ifdef CONFIG\_NATIVE\_APPLICATION

132 #error "ARC MWDT doesn't support building Zephyr as an native application"

133#endif /\* CONFIG\_NATIVE\_APPLICATION \*/

134

135

136#define \_\_no\_optimization \_\_attribute\_\_((optnone))

137#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

138

139#define TOOLCHAIN\_HAS\_C\_GENERIC 1

140#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

141

142#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

143

144#undef BUILD\_ASSERT

145#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201103L)

146#define BUILD\_ASSERT(EXPR, MSG...) static\_assert(EXPR, "" MSG)

147#elif defined(\_\_cplusplus)

148/\* For cpp98 \*/

149#define BUILD\_ASSERT(EXPR, MSG...)

150#else

151#define BUILD\_ASSERT(EXPR, MSG...) \_Static\_assert((EXPR), "" MSG)

152#endif

153

154#define \_\_builtin\_arc\_nop() \_nop()

155

156#endif /\* \_ASMLANGUAGE \*/

157

158#endif /\* !\_LINKER \*/

159#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_MWDT\_H\_ \*/

[common.h](common_8h.md)

Common toolchain abstraction.

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [mwdt.h](mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
