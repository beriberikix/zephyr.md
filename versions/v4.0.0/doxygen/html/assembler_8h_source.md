---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/assembler_8h_source.html
original_path: doxygen/html/assembler_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

assembler.h

[Go to the documentation of this file.](assembler_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (C) 2021 Synopsys, Inc. (www.synopsys.com)

4 \*

5 \* Author: Vineet Gupta <vgupta@synopsys.com>

6 \*

7 \* Top level include file providing ISA pseudo-mnemonics for use in assembler

8 \* and inline assembly.

9 \*

10 \* - Helps code reuse across ARC64/ARC32/ARCv2

11 \* e.g. "LDR" maps to 'LD' on 32-bit ISA, 'LDL' on 64-bit ARCv2/ARC64

12 \*

13 \* - Provides emulation with multiple instructions if the case be

14 \* e.g. "DBNZ" implemented using 'SUB' and 'BRNE'

15 \*

16 \* - Looks more complex than it really is: mainly because Kconfig defines

17 \* are not "honored" in inline assembly. So each variant is unconditional

18 \* code in a standalone file with Kconfig based #ifdef'ry here. During the

19 \* build process, the "C" preprocessor runs through this file, leaving

20 \* just the final variant include in code fed to compiler/assembler.

21 \*/

22

23#ifndef \_\_ASM\_ARC\_ASM\_H

24#define \_\_ASM\_ARC\_ASM\_H 1

25

26#ifdef \_ASMLANGUAGE

27

28#if defined(CONFIG\_ISA\_ARCV3) && defined(CONFIG\_64BIT)

29#define ARC\_PTR .xword

30#define ARC\_REGSZ 8

31#define ARC\_REGSHIFT 3

32

33#if defined(\_\_CCAC\_\_)

34#include "[asm-macro-64-bit-mwdt.h](asm-macro-64-bit-mwdt_8h.md)"

35#else

36#include "[asm-macro-64-bit-gnu.h](asm-macro-64-bit-gnu_8h.md)"

37#endif /\* defined(\_\_CCAC\_\_) \*/

38

39#elif defined(CONFIG\_ISA\_ARCV3) && !defined(CONFIG\_64BIT)

40#define ARC\_PTR .word

41#define ARC\_REGSZ 4

42#define ARC\_REGSHIFT 2

43

44#if defined(\_\_CCAC\_\_)

45#include "[asm-macro-32-bit-mwdt.h](asm-macro-32-bit-mwdt_8h.md)"

46#else

47#include "[asm-macro-32-bit-gnu.h](asm-macro-32-bit-gnu_8h.md)"

48#endif /\* defined(\_\_CCAC\_\_) \*/

49

50#else

51#define ARC\_PTR .word

52#define ARC\_REGSZ 4

53#define ARC\_REGSHIFT 2

54

55#if defined(\_\_CCAC\_\_)

56#include "[asm-macro-32-bit-mwdt.h](asm-macro-32-bit-mwdt_8h.md)"

57#else

58#include "[asm-macro-32-bit-gnu.h](asm-macro-32-bit-gnu_8h.md)"

59#endif /\* defined(\_\_CCAC\_\_) \*/

60

61#endif

62

63#else /\* !\_ASMLANGUAGE \*/

64

65#error "asm-compat macroses used not in assembler code!"

66

67#endif /\* \_ASMLANGUAGE \*/

68

69#endif

[asm-macro-32-bit-gnu.h](asm-macro-32-bit-gnu_8h.md)

[asm-macro-32-bit-mwdt.h](asm-macro-32-bit-mwdt_8h.md)

[asm-macro-64-bit-gnu.h](asm-macro-64-bit-gnu_8h.md)

[asm-macro-64-bit-mwdt.h](asm-macro-64-bit-mwdt_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [assembler.h](assembler_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
