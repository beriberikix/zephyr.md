---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linker-tool-gcc_8h_source.html
original_path: doxygen/html/linker-tool-gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-gcc.h

[Go to the documentation of this file.](linker-tool-gcc_8h.md)

1/\*

2 \* Copyright (c) 2013-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_GCC\_H\_

16#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_GCC\_H\_

17

18#include <[zephyr/kernel/mm.h](kernel_2mm_8h.md)>

19

20#if defined(CONFIG\_ARM)

21 #if defined(CONFIG\_BIG\_ENDIAN)

22 #define OUTPUT\_FORMAT\_ "elf32-bigarm"

23 #else

24 #define OUTPUT\_FORMAT\_ "elf32-littlearm"

25 #endif

26 OUTPUT\_FORMAT(OUTPUT\_FORMAT\_)

27#elif defined(CONFIG\_ARM64)

28 OUTPUT\_FORMAT("elf64-littleaarch64")

29#elif defined(CONFIG\_ARC)

30 #if defined(CONFIG\_ISA\_ARCV3) && defined(CONFIG\_64BIT)

31 OUTPUT\_FORMAT("elf64-littlearc64")

32 #elif defined(CONFIG\_ISA\_ARCV3) && !defined(CONFIG\_64BIT)

33 OUTPUT\_FORMAT("elf32-littlearc64")

34 #else

35 OUTPUT\_FORMAT("elf32-littlearc", "elf32-bigarc", "elf32-littlearc")

36 #endif

37#elif defined(CONFIG\_X86)

38 #if defined(CONFIG\_X86\_64)

39 OUTPUT\_FORMAT("elf64-x86-64")

40 OUTPUT\_ARCH("i386:x86-64")

41 #else

42 OUTPUT\_FORMAT("elf32-i386", "elf32-i386", "elf32-i386")

43 OUTPUT\_ARCH("i386")

44 #endif

45#elif defined(CONFIG\_NIOS2)

46 OUTPUT\_FORMAT("elf32-littlenios2", "elf32-bignios2", "elf32-littlenios2")

47#elif defined(CONFIG\_RISCV)

48 OUTPUT\_ARCH("riscv")

49#ifdef CONFIG\_64BIT

50 OUTPUT\_FORMAT("elf64-littleriscv")

51#else

52 OUTPUT\_FORMAT("elf32-littleriscv")

53#endif

54#elif defined(CONFIG\_XTENSA)

55 /\* Not needed \*/

56#elif defined(CONFIG\_MIPS)

57 OUTPUT\_ARCH("mips")

58#elif defined(CONFIG\_ARCH\_POSIX)

59 /\* Not needed \*/

60#elif defined(CONFIG\_SPARC)

61 OUTPUT\_FORMAT("elf32-sparc")

62#else

63 #error Arch not supported.

64#endif

65

66/\*

67 \* The GROUP\_START() and GROUP\_END() macros are used to define a group

68 \* of sections located in one memory area, such as RAM, ROM, etc.

69 \* The <where> parameter is the name of the memory area.

70 \*/

[ 71](linker-tool-gcc_8h.md#a7461001a81999ec4da41a0f1027c4bbd)#define GROUP\_START(where)

[ 72](linker-tool-gcc_8h.md#ab29c47f59ee5a5456a5f81a9050b1a47)#define GROUP\_END(where)

73

90#if defined(CONFIG\_ARCH\_POSIX)

91#define GROUP\_LINK\_IN(where)

92#elif !defined(K\_MEM\_IS\_VM\_KERNEL)

[ 93](linker-tool-gcc_8h.md#a9250789b7dcbb7afd371010fb3a6031d)#define GROUP\_LINK\_IN(where) > where

94#endif

95

114#if defined(CONFIG\_ARCH\_POSIX)

115#define GROUP\_ROM\_LINK\_IN(vregion, lregion)

116#elif defined(K\_MEM\_IS\_VM\_KERNEL)

117#define GROUP\_ROM\_LINK\_IN(vregion, lregion) > vregion AT > lregion

118#else

119#define GROUP\_ROM\_LINK\_IN(vregion, lregion) > lregion

120#endif

121

134#if defined(CONFIG\_ARCH\_POSIX)

135#define GROUP\_DATA\_LINK\_IN(vregion, lregion)

136#elif defined(CONFIG\_XIP) || defined(K\_MEM\_IS\_VM\_KERNEL)

137#define GROUP\_DATA\_LINK\_IN(vregion, lregion) > vregion AT > lregion

138#else

[ 139](linker-tool-gcc_8h.md#a639d450cbafa51e8937d90df449b797f)#define GROUP\_DATA\_LINK\_IN(vregion, lregion) > vregion

140#endif

141

152#if defined(CONFIG\_ARCH\_POSIX)

153#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion)

154#elif defined(K\_MEM\_IS\_VM\_KERNEL)

155#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion) > vregion AT > lregion

156#elif defined(CONFIG\_XIP)

157#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion) > vregion AT > vregion

158#else

[ 159](linker-tool-gcc_8h.md#a6784ceba92d50f9785cfd130b4341dae)#define GROUP\_NOLOAD\_LINK\_IN(vregion, lregion) > vregion

160#endif

161

175#ifdef K\_MEM\_IS\_VM\_KERNEL

176/\* If we have a virtual memory map we need ALIGN\_WITH\_INPUT in all sections \*/

177#define SECTION\_PROLOGUE(name, options, align) \

178 name options : ALIGN\_WITH\_INPUT align

179#else

[ 180](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)#define SECTION\_PROLOGUE(name, options, align) \

181 name options : align

182#endif

183

201#if defined(CONFIG\_XIP)

202#define SECTION\_DATA\_PROLOGUE(name, options, align) \

203 name options : ALIGN\_WITH\_INPUT

204#else

[ 205](linker-tool-gcc_8h.md#a0d8981d3817b2563846735c90d50240c)#define SECTION\_DATA\_PROLOGUE(name, options, align) \

206 SECTION\_PROLOGUE(name, options, align)

207#endif

208

[ 209](linker-tool-gcc_8h.md#aa5f3d8dcfb378cdbf899467c01494a6f)#define COMMON\_SYMBOLS \*(COMMON)

210

211#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_GCC\_H\_ \*/

[mm.h](kernel_2mm_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-gcc.h](linker-tool-gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
