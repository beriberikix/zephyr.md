---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sections_8h_source.html
original_path: doxygen/html/sections_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

80#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

81#define BOOT\_TEXT\_SECTION\_NAME boot\_text

82#define BOOT\_BSS\_SECTION\_NAME boot\_bss

83#define BOOT\_RODATA\_SECTION\_NAME boot\_rodata

84#define BOOT\_DATA\_SECTION\_NAME boot\_data

85#define BOOT\_NOINIT\_SECTION\_NAME boot\_noinit

86#endif

87

88#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

89#define PINNED\_TEXT\_SECTION\_NAME pinned\_text

90#define PINNED\_BSS\_SECTION\_NAME pinned\_bss

91#define PINNED\_RODATA\_SECTION\_NAME pinned\_rodata

92#define PINNED\_DATA\_SECTION\_NAME pinned\_data

93#define PINNED\_NOINIT\_SECTION\_NAME pinned\_noinit

94#endif

95

96/\* Short section references for use in ASM files \*/

97#if defined(\_ASMLANGUAGE)

98/\* Various text section names \*/

99#define TEXT text

100

101/\* Various data type section names \*/

102#define BSS bss

103#define RODATA rodata

104#define DATA data

105#define NOINIT noinit

106

107#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

108#define BOOT\_TEXT BOOT\_TEXT\_SECTION\_NAME

109#define BOOT\_BSS BOOT\_BSS\_SECTION\_NAME

110#define BOOT\_RODATA BOOT\_RODATA\_SECTION\_NAME

111#define BOOT\_DATA BOOT\_DATA\_SECTION\_NAME

112#define BOOT\_NOINIT BOOT\_NOINIT\_SECTION\_NAME

113#else

114#define BOOT\_TEXT TEXT

115#define BOOT\_BSS BSS

116#define BOOT\_RODATA RODATA

117#define BOOT\_DATA DATA

118#define BOOT\_NOINIT NOINIT

119#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

120

121#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

122#define PINNED\_TEXT PINNED\_TEXT\_SECTION\_NAME

123#define PINNED\_BSS PINNED\_BSS\_SECTION\_NAME

124#define PINNED\_RODATA PINNED\_RODATA\_SECTION\_NAME

125#define PINNED\_DATA PINNED\_DATA\_SECTION\_NAME

126#define PINNED\_NOINIT PINNED\_NOINIT\_SECTION\_NAME

127#else

128#define PINNED\_TEXT TEXT

129#define PINNED\_BSS BSS

130#define PINNED\_RODATA RODATA

131#define PINNED\_DATA DATA

132#define PINNED\_NOINIT NOINIT

133#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

134

135#endif /\* \_ASMLANGUAGE \*/

136

137#include <[zephyr/linker/section\_tags.h](section__tags_8h.md)>

138

139#endif /\* ZEPHYR\_INCLUDE\_LINKER\_SECTIONS\_H\_ \*/

[section\_tags.h](section__tags_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [sections.h](sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
