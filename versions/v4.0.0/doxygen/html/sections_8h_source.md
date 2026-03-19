---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sections_8h_source.html
original_path: doxygen/html/sections_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sections.h

[Go to the documentation of this file.](sections_8h.md)

1/\*

2 \* Copyright (c) 2013-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_LINKER\_SECTIONS\_H\_

16#define ZEPHYR\_INCLUDE\_LINKER\_SECTIONS\_H\_

17

18#define \_TEXT\_SECTION\_NAME text

19#define \_RODATA\_SECTION\_NAME rodata

20#define \_CTOR\_SECTION\_NAME ctors

21/\* Linker issue with XIP where the name "data" cannot be used \*/

22#define \_DATA\_SECTION\_NAME datas

23#define \_BSS\_SECTION\_NAME bss

24#define \_NOINIT\_SECTION\_NAME noinit

25

26#define \_APP\_SMEM\_SECTION\_NAME app\_smem

27#define \_APP\_DATA\_SECTION\_NAME app\_datas

28#define \_APP\_BSS\_SECTION\_NAME app\_bss

29#define \_APP\_NOINIT\_SECTION\_NAME app\_noinit

30

31#define \_APP\_SMEM\_PINNED\_SECTION\_NAME app\_smem\_pinned

32

33#define \_UNDEFINED\_SECTION\_NAME undefined

34

35/\* Interrupts \*/

36#define \_IRQ\_VECTOR\_TABLE\_SECTION\_NAME .gnu.linkonce.irq\_vector\_table

37#define \_IRQ\_VECTOR\_TABLE\_SECTION\_SYMS .gnu.linkonce.irq\_vector\_table\*

38

39#define \_SW\_ISR\_TABLE\_SECTION\_NAME .gnu.linkonce.sw\_isr\_table

40#define \_SW\_ISR\_TABLE\_SECTION\_SYMS .gnu.linkonce.sw\_isr\_table\*

41

42#ifdef CONFIG\_SHARED\_INTERRUPTS

43#define \_SHARED\_SW\_ISR\_TABLE\_SECTION\_NAME .gnu.linkonce.shared\_sw\_isr\_table

44#define \_SHARED\_SW\_ISR\_TABLE\_SECTION\_SYMS .gnu.linkonce.shared\_sw\_isr\_table\*

45#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

46

47/\* Architecture-specific sections \*/

48#if defined(CONFIG\_ARM)

49#define \_KINETIS\_FLASH\_CONFIG\_SECTION\_NAME kinetis\_flash\_config

50#define \_TI\_CCFG\_SECTION\_NAME .ti\_ccfg

51

52#define \_CCM\_DATA\_SECTION\_NAME .ccm\_data

53#define \_CCM\_BSS\_SECTION\_NAME .ccm\_bss

54#define \_CCM\_NOINIT\_SECTION\_NAME .ccm\_noinit

55

56#define \_ITCM\_SECTION\_NAME .itcm

57

58#define \_DTCM\_DATA\_SECTION\_NAME .dtcm\_data

59#define \_DTCM\_BSS\_SECTION\_NAME .dtcm\_bss

60#define \_DTCM\_NOINIT\_SECTION\_NAME .dtcm\_noinit

61

62#define \_OCM\_DATA\_SECTION\_NAME .ocm\_data

63#define \_OCM\_BSS\_SECTION\_NAME .ocm\_bss

64#endif

65

66#define \_IMX\_BOOT\_CONF\_SECTION\_NAME .boot\_hdr.conf

67#define \_IMX\_BOOT\_DATA\_SECTION\_NAME .boot\_hdr.data

68#define \_IMX\_BOOT\_IVT\_SECTION\_NAME .boot\_hdr.ivt

69#define \_IMX\_BOOT\_DCD\_SECTION\_NAME .boot\_hdr.dcd\_data

70#define \_IMX\_BOOT\_CONTAINER\_SECTION\_NAME .boot\_hdr.container

71

72#define \_STM32\_SDRAM1\_SECTION\_NAME .stm32\_sdram1

73#define \_STM32\_SDRAM2\_SECTION\_NAME .stm32\_sdram2

74

75#define \_STM32\_BACKUP\_SRAM\_SECTION\_NAME .stm32\_backup\_sram

76

77#ifdef CONFIG\_NOCACHE\_MEMORY

78#define \_NOCACHE\_SECTION\_NAME nocache

79#endif

80

81/\* Symbol table section \*/

82#if defined(CONFIG\_SYMTAB)

83#define \_SYMTAB\_INFO\_SECTION\_NAME .gnu.linkonce.symtab.info

84#define \_SYMTAB\_ENTRY\_SECTION\_NAME .gnu.linkonce.symtab.entry

85#define \_SYMTAB\_SECTION\_SYMS .gnu.linkonce.symtab\*

86#endif /\* CONFIG\_SYMTAB \*/

87

88#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

89#define BOOT\_TEXT\_SECTION\_NAME boot\_text

90#define BOOT\_BSS\_SECTION\_NAME boot\_bss

91#define BOOT\_RODATA\_SECTION\_NAME boot\_rodata

92#define BOOT\_DATA\_SECTION\_NAME boot\_data

93#define BOOT\_NOINIT\_SECTION\_NAME boot\_noinit

94#endif

95

96#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

97#define PINNED\_TEXT\_SECTION\_NAME pinned\_text

98#define PINNED\_BSS\_SECTION\_NAME pinned\_bss

99#define PINNED\_RODATA\_SECTION\_NAME pinned\_rodata

100#define PINNED\_DATA\_SECTION\_NAME pinned\_data

101#define PINNED\_NOINIT\_SECTION\_NAME pinned\_noinit

102#endif

103

104#if defined(CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION)

105#define ONDEMAND\_TEXT\_SECTION\_NAME ondemand\_text

106#define ONDEMAND\_RODATA\_SECTION\_NAME ondemand\_rodata

107#endif

108

109/\* Short section references for use in ASM files \*/

110#if defined(\_ASMLANGUAGE)

111/\* Various text section names \*/

112#define TEXT text

113

114/\* Various data type section names \*/

115#define BSS bss

116#define RODATA rodata

117#define DATA data

118#define NOINIT noinit

119

120#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

121#define BOOT\_TEXT BOOT\_TEXT\_SECTION\_NAME

122#define BOOT\_BSS BOOT\_BSS\_SECTION\_NAME

123#define BOOT\_RODATA BOOT\_RODATA\_SECTION\_NAME

124#define BOOT\_DATA BOOT\_DATA\_SECTION\_NAME

125#define BOOT\_NOINIT BOOT\_NOINIT\_SECTION\_NAME

126#else

127#define BOOT\_TEXT TEXT

128#define BOOT\_BSS BSS

129#define BOOT\_RODATA RODATA

130#define BOOT\_DATA DATA

131#define BOOT\_NOINIT NOINIT

132#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

133

134#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

135#define PINNED\_TEXT PINNED\_TEXT\_SECTION\_NAME

136#define PINNED\_BSS PINNED\_BSS\_SECTION\_NAME

137#define PINNED\_RODATA PINNED\_RODATA\_SECTION\_NAME

138#define PINNED\_DATA PINNED\_DATA\_SECTION\_NAME

139#define PINNED\_NOINIT PINNED\_NOINIT\_SECTION\_NAME

140#else

141#define PINNED\_TEXT TEXT

142#define PINNED\_BSS BSS

143#define PINNED\_RODATA RODATA

144#define PINNED\_DATA DATA

145#define PINNED\_NOINIT NOINIT

146#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

147

148#if defined(CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION)

149#define ONDEMAND\_TEXT ONDEMAND\_TEXT\_SECTION\_NAME

150#define ONDEMAND\_RODATA ONDEMAND\_RODATA\_SECTION\_NAME

151#else

152#define ONDEMAND\_TEXT TEXT

153#define ONDEMAND\_RODATA RODATA

154#endif /\* CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION \*/

155

156#endif /\* \_ASMLANGUAGE \*/

157

158#include <[zephyr/linker/section\_tags.h](section__tags_8h.md)>

159

160#endif /\* ZEPHYR\_INCLUDE\_LINKER\_SECTIONS\_H\_ \*/

[section\_tags.h](section__tags_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [sections.h](sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
