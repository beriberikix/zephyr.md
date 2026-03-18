---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sections_8h_source.html
original_path: doxygen/html/sections_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

70

71#define \_STM32\_SDRAM1\_SECTION\_NAME .stm32\_sdram1

72#define \_STM32\_SDRAM2\_SECTION\_NAME .stm32\_sdram2

73

74#define \_STM32\_BACKUP\_SRAM\_SECTION\_NAME .stm32\_backup\_sram

75

76#ifdef CONFIG\_NOCACHE\_MEMORY

77#define \_NOCACHE\_SECTION\_NAME nocache

78#endif

79

80/\* Symbol table section \*/

81#if defined(CONFIG\_SYMTAB)

82#define \_SYMTAB\_INFO\_SECTION\_NAME .gnu.linkonce.symtab.info

83#define \_SYMTAB\_ENTRY\_SECTION\_NAME .gnu.linkonce.symtab.entry

84#define \_SYMTAB\_SECTION\_SYMS .gnu.linkonce.symtab\*

85#endif /\* CONFIG\_SYMTAB \*/

86

87#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

88#define BOOT\_TEXT\_SECTION\_NAME boot\_text

89#define BOOT\_BSS\_SECTION\_NAME boot\_bss

90#define BOOT\_RODATA\_SECTION\_NAME boot\_rodata

91#define BOOT\_DATA\_SECTION\_NAME boot\_data

92#define BOOT\_NOINIT\_SECTION\_NAME boot\_noinit

93#endif

94

95#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

96#define PINNED\_TEXT\_SECTION\_NAME pinned\_text

97#define PINNED\_BSS\_SECTION\_NAME pinned\_bss

98#define PINNED\_RODATA\_SECTION\_NAME pinned\_rodata

99#define PINNED\_DATA\_SECTION\_NAME pinned\_data

100#define PINNED\_NOINIT\_SECTION\_NAME pinned\_noinit

101#endif

102

103/\* Short section references for use in ASM files \*/

104#if defined(\_ASMLANGUAGE)

105/\* Various text section names \*/

106#define TEXT text

107

108/\* Various data type section names \*/

109#define BSS bss

110#define RODATA rodata

111#define DATA data

112#define NOINIT noinit

113

114#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

115#define BOOT\_TEXT BOOT\_TEXT\_SECTION\_NAME

116#define BOOT\_BSS BOOT\_BSS\_SECTION\_NAME

117#define BOOT\_RODATA BOOT\_RODATA\_SECTION\_NAME

118#define BOOT\_DATA BOOT\_DATA\_SECTION\_NAME

119#define BOOT\_NOINIT BOOT\_NOINIT\_SECTION\_NAME

120#else

121#define BOOT\_TEXT TEXT

122#define BOOT\_BSS BSS

123#define BOOT\_RODATA RODATA

124#define BOOT\_DATA DATA

125#define BOOT\_NOINIT NOINIT

126#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

127

128#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

129#define PINNED\_TEXT PINNED\_TEXT\_SECTION\_NAME

130#define PINNED\_BSS PINNED\_BSS\_SECTION\_NAME

131#define PINNED\_RODATA PINNED\_RODATA\_SECTION\_NAME

132#define PINNED\_DATA PINNED\_DATA\_SECTION\_NAME

133#define PINNED\_NOINIT PINNED\_NOINIT\_SECTION\_NAME

134#else

135#define PINNED\_TEXT TEXT

136#define PINNED\_BSS BSS

137#define PINNED\_RODATA RODATA

138#define PINNED\_DATA DATA

139#define PINNED\_NOINIT NOINIT

140#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

141

142#endif /\* \_ASMLANGUAGE \*/

143

144#include <[zephyr/linker/section\_tags.h](section__tags_8h.md)>

145

146#endif /\* ZEPHYR\_INCLUDE\_LINKER\_SECTIONS\_H\_ \*/

[section\_tags.h](section__tags_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [sections.h](sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
