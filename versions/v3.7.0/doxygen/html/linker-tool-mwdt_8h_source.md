---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/linker-tool-mwdt_8h_source.html
original_path: doxygen/html/linker-tool-mwdt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-mwdt.h

[Go to the documentation of this file.](linker-tool-mwdt_8h.md)

1/\*

2 \* Copyright (c) 2020, Synopsys, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_MWDT\_H\_

16#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_MWDT\_H\_

17

18/\*

19 \* mwdt linker doesn't have the following directives

20 \*/

[ 21](linker-tool-mwdt_8h.md#a0a3e46fec8345ab664843141b78b82a3)#define ASSERT(x, y)

[ 22](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)#define SUBALIGN(x) ALIGN(x)

23

24/\*

25 \* The GROUP\_START() and GROUP\_END() macros are used to define a group

26 \* of sections located in one memory area, such as RAM, ROM, etc.

27 \* The <where> parameter is the name of the memory area.

28 \*/

[ 29](linker-tool-mwdt_8h.md#a7461001a81999ec4da41a0f1027c4bbd)#define GROUP\_START(where)

[ 30](linker-tool-mwdt_8h.md#ab29c47f59ee5a5456a5f81a9050b1a47)#define GROUP\_END(where)

31

32/\*

33 \* The GROUP\_LINK\_IN() macro is located at the end of the section

34 \* description and tells the linker that this section is located in

35 \* the memory area specified by <where> argument.

36 \*/

[ 37](linker-tool-mwdt_8h.md#a9250789b7dcbb7afd371010fb3a6031d)#define GROUP\_LINK\_IN(where) > where

38

45#define GROUP\_ROM\_LINK\_IN(vregion, lregion) > lregion

46

47/\*

48 \* As GROUP\_LINK\_IN(), but takes a second argument indicating the

49 \* memory region (e.g. "ROM") for the load address. Used for

50 \* initialized data sections that on XIP platforms must be copied at

51 \* startup.

52 \*

53 \* And, because output directives in GNU ld are "sticky", this must

54 \* also be used on the first section \*after\* such an initialized data

55 \* section, specifying the same memory region (e.g. "RAM") for both

56 \* vregion and lregion.

57 \*/

58#ifdef CONFIG\_XIP

59#define GROUP\_DATA\_LINK\_IN(vregion, lregion) > vregion AT > lregion

60#else

[ 61](linker-tool-mwdt_8h.md#a639d450cbafa51e8937d90df449b797f)#define GROUP\_DATA\_LINK\_IN(vregion, lregion) > vregion

62#endif

63

68#ifdef CONFIG\_XIP

69#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion) > vregion AT > vregion

70#else

[ 71](linker-tool-mwdt_8h.md#a6784ceba92d50f9785cfd130b4341dae)#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion) > vregion

72#endif

73

74/\*

75 \* The SECTION\_PROLOGUE() macro is used to define the beginning of a section.

76 \* The <name> parameter is the name of the section, and the <option> parameter

77 \* is to include any special options such as (NOLOAD). Page alignment has its

78 \* own parameter since it needs abstraction across the different toolchains.

79 \* If not required, the <options> and <align> parameters should be left blank.

80 \*/

[ 81](linker-tool-mwdt_8h.md#a784c696b95848c5f070e257a50fbe23a)#define SECTION\_PROLOGUE(name, options, align) name options : align

82

83/\*

84 \* As for SECTION\_PROLOGUE(), except that this one must (!) be used

85 \* for data sections which on XIP platforms will have differing

86 \* virtual and load addresses (i.e. they'll be copied into RAM at

87 \* program startup). Such a section must (!) also use

88 \* GROUP\_LINK\_IN\_LMA to specify the correct output load address.

89 \*/

90#ifdef CONFIG\_XIP

91#define SECTION\_DATA\_PROLOGUE(name, options, align) \

92 name options ALIGN(8) : align

93#else

[ 94](linker-tool-mwdt_8h.md#a0d8981d3817b2563846735c90d50240c)#define SECTION\_DATA\_PROLOGUE(name, options, align) name options : align

95

96#endif

97

[ 98](linker-tool-mwdt_8h.md#afd4796dcd7496f1463f849165f7e2779)#define SORT\_BY\_NAME(x) SORT(x)

99

100#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_MWDT\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-mwdt.h](linker-tool-mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
