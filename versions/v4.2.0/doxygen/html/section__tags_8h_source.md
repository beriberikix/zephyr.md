---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/section__tags_8h_source.html
original_path: doxygen/html/section__tags_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

section\_tags.h

[Go to the documentation of this file.](section__tags_8h.md)

1/\* Macros for tagging symbols and putting them in the correct sections. \*/

2

3/\*

4 \* Copyright (c) 2013-2014, Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_LINKER\_SECTION\_TAGS\_H\_

10#define ZEPHYR\_INCLUDE\_LINKER\_SECTION\_TAGS\_H\_

11

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13

14#if !defined(\_ASMLANGUAGE)

15

16#include <[zephyr/linker/sections.h](sections_8h.md)>

17

18#define \_\_noinit \_\_in\_section\_unique(\_NOINIT\_SECTION\_NAME)

19#define \_\_noinit\_named(name) \_\_in\_section\_unique\_named(\_NOINIT\_SECTION\_NAME, name)

20#define \_\_irq\_vector\_table Z\_GENERIC\_SECTION(\_IRQ\_VECTOR\_TABLE\_SECTION\_NAME)

21#define \_\_sw\_isr\_table Z\_GENERIC\_SECTION(\_SW\_ISR\_TABLE\_SECTION\_NAME)

22

23#ifdef CONFIG\_SHARED\_INTERRUPTS

24#define \_\_shared\_sw\_isr\_table Z\_GENERIC\_SECTION(\_SHARED\_SW\_ISR\_TABLE\_SECTION\_NAME)

25#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

26

27/\* Attribute macros to place code and data into IMR memory \*/

28#define \_\_imr \_\_in\_section\_unique(imr)

29#define \_\_imrdata \_\_in\_section\_unique(imrdata)

30

31#if defined(CONFIG\_ARM)

32#define \_\_kinetis\_flash\_config\_section \_\_in\_section\_unique(\_KINETIS\_FLASH\_CONFIG\_SECTION\_NAME)

33#define \_\_ti\_ccfg\_section Z\_GENERIC\_SECTION(\_TI\_CCFG\_SECTION\_NAME)

34#define \_\_ccm\_data\_section Z\_GENERIC\_SECTION(\_CCM\_DATA\_SECTION\_NAME)

35#define \_\_ccm\_bss\_section Z\_GENERIC\_SECTION(\_CCM\_BSS\_SECTION\_NAME)

36#define \_\_ccm\_noinit\_section Z\_GENERIC\_SECTION(\_CCM\_NOINIT\_SECTION\_NAME)

37#define \_\_itcm\_section Z\_GENERIC\_SECTION(\_ITCM\_SECTION\_NAME)

38#define \_\_dtcm\_data\_section Z\_GENERIC\_SECTION(\_DTCM\_DATA\_SECTION\_NAME)

39#define \_\_dtcm\_bss\_section Z\_GENERIC\_SECTION(\_DTCM\_BSS\_SECTION\_NAME)

40#define \_\_dtcm\_noinit\_section Z\_GENERIC\_SECTION(\_DTCM\_NOINIT\_SECTION\_NAME)

41#define \_\_ocm\_data\_section Z\_GENERIC\_SECTION(\_OCM\_DATA\_SECTION\_NAME)

42#define \_\_ocm\_bss\_section Z\_GENERIC\_SECTION(\_OCM\_BSS\_SECTION\_NAME)

43#define \_\_imx\_boot\_conf\_section Z\_GENERIC\_SECTION(\_IMX\_BOOT\_CONF\_SECTION\_NAME)

44#define \_\_imx\_boot\_data\_section Z\_GENERIC\_SECTION(\_IMX\_BOOT\_DATA\_SECTION\_NAME)

45#define \_\_imx\_boot\_ivt\_section Z\_GENERIC\_SECTION(\_IMX\_BOOT\_IVT\_SECTION\_NAME)

46#define \_\_imx\_boot\_dcd\_section Z\_GENERIC\_SECTION(\_IMX\_BOOT\_DCD\_SECTION\_NAME)

47#define \_\_imx\_boot\_container\_section Z\_GENERIC\_SECTION(\_IMX\_BOOT\_CONTAINER\_SECTION\_NAME)

48#define \_\_stm32\_sdram1\_section Z\_GENERIC\_SECTION(\_STM32\_SDRAM1\_SECTION\_NAME)

49#define \_\_stm32\_sdram2\_section Z\_GENERIC\_SECTION(\_STM32\_SDRAM2\_SECTION\_NAME)

50#define \_\_stm32\_psram\_section Z\_GENERIC\_SECTION(\_STM32\_PSRAM\_SECTION\_NAME)

51#define \_\_stm32\_backup\_sram\_section Z\_GENERIC\_SECTION(\_STM32\_BACKUP\_SRAM\_SECTION\_NAME)

52#endif /\* CONFIG\_ARM \*/

53

54#if defined(CONFIG\_NOCACHE\_MEMORY)

55#define \_\_nocache \_\_in\_section\_unique(\_NOCACHE\_SECTION\_NAME)

56#define \_\_nocache\_noinit \_\_nocache

57#else

58#define \_\_nocache

59#define \_\_nocache\_noinit \_\_noinit

60#endif /\* CONFIG\_NOCACHE\_MEMORY \*/

61

62#if defined(CONFIG\_KERNEL\_COHERENCE)

63#define \_\_incoherent \_\_in\_section\_unique(cached)

64#if defined(CONFIG\_USERSPACE)

65#define \_\_stackmem Z\_GENERIC\_SECTION(.user\_stacks)

66#else

67#define \_\_stackmem \_\_incoherent

68#endif /\* CONFIG\_USERSPACE \*/

69#define \_\_kstackmem \_\_incoherent

70#else

71#define \_\_incoherent

72#define \_\_stackmem Z\_GENERIC\_SECTION(.user\_stacks)

73#define \_\_kstackmem \_\_noinit

74#endif /\* CONFIG\_KERNEL\_COHERENCE \*/

75

76#if defined(CONFIG\_LINKER\_USE\_BOOT\_SECTION)

77#define \_\_boot\_func Z\_GENERIC\_DOT\_SECTION(BOOT\_TEXT\_SECTION\_NAME)

78#define \_\_boot\_data Z\_GENERIC\_DOT\_SECTION(BOOT\_DATA\_SECTION\_NAME)

79#define \_\_boot\_rodata Z\_GENERIC\_DOT\_SECTION(BOOT\_RODATA\_SECTION\_NAME)

80#define \_\_boot\_bss Z\_GENERIC\_DOT\_SECTION(BOOT\_BSS\_SECTION\_NAME)

81#define \_\_boot\_noinit Z\_GENERIC\_DOT\_SECTION(BOOT\_NOINIT\_SECTION\_NAME)

82#else

83#define \_\_boot\_func

84#define \_\_boot\_data

85#define \_\_boot\_rodata

86#define \_\_boot\_bss

87#define \_\_boot\_noinit \_\_noinit

88#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

89

90#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

91#define \_\_pinned\_func Z\_GENERIC\_DOT\_SECTION(PINNED\_TEXT\_SECTION\_NAME)

92#define \_\_pinned\_data Z\_GENERIC\_DOT\_SECTION(PINNED\_DATA\_SECTION\_NAME)

93#define \_\_pinned\_rodata Z\_GENERIC\_DOT\_SECTION(PINNED\_RODATA\_SECTION\_NAME)

94#define \_\_pinned\_bss Z\_GENERIC\_DOT\_SECTION(PINNED\_BSS\_SECTION\_NAME)

95#define \_\_pinned\_noinit Z\_GENERIC\_DOT\_SECTION(PINNED\_NOINIT\_SECTION\_NAME)

96#else

97#define \_\_pinned\_func

98#define \_\_pinned\_data

99#define \_\_pinned\_rodata

100#define \_\_pinned\_bss

101#define \_\_pinned\_noinit \_\_noinit

102#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

103

104#if defined(CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION)

105#define \_\_ondemand\_func Z\_GENERIC\_DOT\_SECTION(ONDEMAND\_TEXT\_SECTION\_NAME)

106#define \_\_ondemand\_rodata Z\_GENERIC\_DOT\_SECTION(ONDEMAND\_RODATA\_SECTION\_NAME)

107#else

108#define \_\_ondemand\_func

109#define \_\_ondemand\_rodata

110#endif /\* CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION \*/

111

112#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

113#define \_\_isr \_\_pinned\_func

114#else

115#define \_\_isr

116#endif

117

118/\* Symbol table section \*/

119#if defined(CONFIG\_SYMTAB)

120#define \_\_symtab\_info Z\_GENERIC\_SECTION(\_SYMTAB\_INFO\_SECTION\_NAME)

121#define \_\_symtab\_entry Z\_GENERIC\_SECTION(\_SYMTAB\_ENTRY\_SECTION\_NAME)

122#endif /\* CONFIG\_SYMTAB \*/

123

124#endif /\* !\_ASMLANGUAGE \*/

125

126#endif /\* ZEPHYR\_INCLUDE\_LINKER\_SECTION\_TAGS\_H\_ \*/

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [section\_tags.h](section__tags_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
