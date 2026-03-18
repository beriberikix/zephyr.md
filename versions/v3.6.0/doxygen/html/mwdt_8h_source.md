---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mwdt_8h_source.html
original_path: doxygen/html/mwdt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23.macro section\_var\_mwdt, section, symbol

24 .section .\&section\&.\&symbol, "aw"

25 symbol :

26.endm

27

28.macro section\_func\_mwdt, section, symbol

29 .section .\&section\&.\&symbol, "ax"

30 FUNC\_CODE()

31 PERFOPT\_ALIGN

32 symbol :

33 FUNC\_INSTR(symbol)

34.endm

35

36.macro section\_subsec\_func\_mwdt, section, subsection, symbol

37 .section .\&section\&.\&subsection, "ax"

38 PERFOPT\_ALIGN

39 symbol :

40.endm

41

42#define SECTION\_VAR(sect, sym) section\_var\_mwdt sect, sym

43#define SECTION\_FUNC(sect, sym) section\_func\_mwdt sect, sym

44#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

45 section\_subsec\_func\_mwdt sect, subsec, sym

46

47.macro glbl\_text\_mwdt, symbol

48 .globl symbol

49 .type symbol, @function

50.endm

51

52.macro glbl\_data\_mwdt, symbol

53 .globl symbol

54 .type symbol, @object

55.endm

56

57.macro weak\_data\_mwdt, symbol

58 .weak symbol

59 .type symbol, @object

60.endm

61

62#define GTEXT(sym) glbl\_text\_mwdt sym

63#define GDATA(sym) glbl\_data\_mwdt sym

64#define WDATA(sym) weak\_data\_mwdt sym

65

66#else /\* defined(\_ASMLANGUAGE) \*/

67

68/\* MWDT toolchain misses ssize\_t definition which is used by Zephyr \*/

69#ifndef \_SSIZE\_T\_DEFINED

70#define \_SSIZE\_T\_DEFINED

71#ifdef CONFIG\_64BIT

72 typedef long [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

73#else

74 typedef int [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

75#endif

76#endif /\* \_SSIZE\_T\_DEFINED \*/

77

78#ifdef CONFIG\_NEWLIB\_LIBC

79 #error "ARC MWDT doesn't support building with CONFIG\_NEWLIB\_LIBC as it doesn't have newlib"

80#endif /\* CONFIG\_NEWLIB\_LIBC \*/

81

82#ifdef CONFIG\_NATIVE\_APPLICATION

83 #error "ARC MWDT doesn't support building Zephyr as an native application"

84#endif /\* CONFIG\_NATIVE\_APPLICATION \*/

85

86

87#define \_\_no\_optimization \_\_attribute\_\_((optnone))

88#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

89

90#define TOOLCHAIN\_HAS\_C\_GENERIC 1

91#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

92

93#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

94

95#undef BUILD\_ASSERT

96#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201103L)

97#define BUILD\_ASSERT(EXPR, MSG...) static\_assert(EXPR, "" MSG)

98#elif defined(\_\_cplusplus)

99/\* For cpp98 \*/

100#define BUILD\_ASSERT(EXPR, MSG...)

101#else

102#define BUILD\_ASSERT(EXPR, MSG...) \_Static\_assert(EXPR, "" MSG)

103#endif

104

105#define \_\_builtin\_arc\_nop() \_nop()

106

107#endif /\* \_ASMLANGUAGE \*/

108

109#endif /\* !\_LINKER \*/

110#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_MWDT\_H\_ \*/

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
