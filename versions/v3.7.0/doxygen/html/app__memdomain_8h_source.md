---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/app__memdomain_8h_source.html
original_path: doxygen/html/app__memdomain_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

app\_memdomain.h

[Go to the documentation of this file.](app__memdomain_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_APP\_MEMORY\_APP\_MEMDOMAIN\_H\_

7#define ZEPHYR\_INCLUDE\_APP\_MEMORY\_APP\_MEMDOMAIN\_H\_

8

9#include <[zephyr/linker/linker-defs.h](linker-defs_8h.md)>

10#include <[zephyr/sys/dlist.h](dlist_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12

19

20#ifdef CONFIG\_USERSPACE

21

[ 30](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)#define K\_APP\_DMEM\_SECTION(id) data\_smem\_##id##\_data

31

[ 40](group__mem__domain__apis__app.md#ga24cb6342261cc6abc76a7809a4170e64)#define K\_APP\_BMEM\_SECTION(id) data\_smem\_##id##\_bss

41

[ 51](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)#define K\_APP\_DMEM(id) Z\_GENERIC\_SECTION(K\_APP\_DMEM\_SECTION(id))

52

[ 61](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)#define K\_APP\_BMEM(id) Z\_GENERIC\_SECTION(K\_APP\_BMEM\_SECTION(id))

62

63struct z\_app\_region {

64 void \*bss\_start;

65 size\_t bss\_size;

66};

67

68#define Z\_APP\_START(id) z\_data\_smem\_##id##\_part\_start

69#define Z\_APP\_SIZE(id) z\_data\_smem\_##id##\_part\_size

70#define Z\_APP\_BSS\_START(id) z\_data\_smem\_##id##\_bss\_start

71#define Z\_APP\_BSS\_SIZE(id) z\_data\_smem\_##id##\_bss\_size

72

73/\* If a partition is declared with K\_APPMEM\_PARTITION, but never has any

74 \* data assigned to its contents, then no symbols with its prefix will end

75 \* up in the symbol table. This prevents gen\_app\_partitions.py from detecting

76 \* that the partition exists, and the linker symbols which specify partition

77 \* bounds will not be generated, resulting in build errors.

78 \*

79 \* What this inline assembly code does is define a symbol with no data.

80 \* This should work for all arches that produce ELF binaries, see

81 \* https://sourceware.org/binutils/docs/as/Section.html

82 \*

83 \* We don't know what active flags/type of the pushed section were, so we are

84 \* specific: "aw" indicates section is allocatable and writable,

85 \* and "@progbits" indicates the section has data.

86 \*/

87#if defined(CONFIG\_ARM) || defined(CONFIG\_ARM64)

88/\* ARM has a quirk in that '@' denotes a comment, so we have to send

89 \* %progbits to the assembler instead.

90 \*/

91#define Z\_PROGBITS\_SYM "%"

92#else

93#define Z\_PROGBITS\_SYM "@"

94#endif

95

96#if defined(CONFIG\_ARC) && defined(\_\_CCAC\_\_)

97/\* ARC MWDT assembler has slightly different pushsection/popsection directives

98 \* names.

99 \*/

100#define Z\_PUSHSECTION\_DIRECTIV ".pushsect"

101#define Z\_POPSECTION\_DIRECTIVE ".popsect"

102#else

103#define Z\_PUSHSECTION\_DIRECTIV ".pushsection"

104#define Z\_POPSECTION\_DIRECTIVE ".popsection"

105#endif

106

107#define Z\_APPMEM\_PLACEHOLDER(name) \

108 \_\_asm\_\_ ( \

109 Z\_PUSHSECTION\_DIRECTIV " " STRINGIFY(K\_APP\_DMEM\_SECTION(name)) \

110 ",\"aw\"," Z\_PROGBITS\_SYM "progbits\n\t" \

111 ".global " STRINGIFY(name) "\_placeholder\n\t" \

112 STRINGIFY(name) "\_placeholder:\n\t" \

113 Z\_POPSECTION\_DIRECTIVE "\n\t")

114

[ 127](group__mem__domain__apis__app.md#gaba1614a7fa1a2ce2fc7cfd6ecfc02796)#define K\_APPMEM\_PARTITION\_DEFINE(name) \

128 extern char Z\_APP\_START(name)[]; \

129 extern char Z\_APP\_SIZE(name)[]; \

130 struct k\_mem\_partition name = { \

131 .start = (uintptr\_t) &Z\_APP\_START(name)[0], \

132 .size = (size\_t) &Z\_APP\_SIZE(name)[0], \

133 .attr = K\_MEM\_PARTITION\_P\_RW\_U\_RW \

134 }; \

135 extern char Z\_APP\_BSS\_START(name)[]; \

136 extern char Z\_APP\_BSS\_SIZE(name)[]; \

137 Z\_GENERIC\_SECTION(.app\_regions.name) \

138 const struct z\_app\_region name##\_region = { \

139 .bss\_start = &Z\_APP\_BSS\_START(name)[0], \

140 .bss\_size = (size\_t) &Z\_APP\_BSS\_SIZE(name)[0] \

141 }; \

142 Z\_APPMEM\_PLACEHOLDER(name)

143#else

144

145#define K\_APP\_BMEM(ptn)

146#define K\_APP\_DMEM(ptn)

147#define K\_APP\_DMEM\_SECTION(ptn) .data

148#define K\_APP\_BMEM\_SECTION(ptn) .bss

149#define K\_APPMEM\_PARTITION\_DEFINE(name)

150

151#endif /\* CONFIG\_USERSPACE \*/

152

156

157#endif /\* ZEPHYR\_INCLUDE\_APP\_MEMORY\_APP\_MEMDOMAIN\_H\_ \*/

[dlist.h](dlist_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[linker-defs.h](linker-defs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [app\_memory](dir_a5c66281f93d933ad709643c33992dc2.md)
- [app\_memdomain.h](app__memdomain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
