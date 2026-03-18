---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2cortex__a__r_2exception_8h_source.html
original_path: doxygen/html/arm_2cortex__a__r_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm_2cortex__a__r_2exception_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_

14

15#ifdef \_ASMLANGUAGE

16GTEXT(z\_arm\_exc\_exit);

17#else

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

25

26/\* Registers s16-s31 (d8-d15, q4-q7) must be preserved across subroutine calls.

27 \*

28 \* Registers s0-s15 (d0-d7, q0-q3) do not have to be preserved (and can be used

29 \* for passing arguments or returning results in standard procedure-call variants).

30 \*

31 \* Registers d16-d31 (q8-q15), do not have to be preserved.

32 \*/

33struct \_\_fpu\_sf {

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) s[16]; /\* s0~s15 (d0-d7) \*/

35#ifdef CONFIG\_VFP\_FEATURE\_REGS\_S64\_D32

36 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)[16]; /\* d16~d31 \*/

37#endif

38 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpscr;

39 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) undefined;

40};

41#endif

42

43/\* Additional register state that is not stacked by hardware on exception

44 \* entry.

45 \*

46 \* These fields are ONLY valid in the ESF copy passed into z\_arm\_fatal\_error().

47 \* When information for a member is unavailable, the field is set to zero.

48 \*/

49#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

50struct \_\_extra\_esf\_info {

51 \_callee\_saved\_t \*callee;

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) msp;

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) exc\_return;

54};

55#endif /\* CONFIG\_EXTRA\_EXCEPTION\_INFO \*/

56

57struct \_\_esf {

58#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

59 struct \_\_extra\_esf\_info extra\_info;

60#endif

61#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

62 struct \_\_fpu\_sf fpu;

63#endif

64 struct \_\_basic\_sf {

65 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a1, r0);

66 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a2, r1);

67 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a3, r2);

68 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a4, r3);

69 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(ip, r12);

70 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(lr, r14);

71 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(pc, r15);

72 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xpsr;

73 } basic;

74};

75

76extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arm\_coredump\_fault\_sp;

77

78typedef struct \_\_esf z\_arch\_esf\_t;

79

80extern void z\_arm\_exc\_exit(bool [fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833));

81

82#ifdef \_\_cplusplus

83}

84#endif

85

86#endif /\* \_ASMLANGUAGE \*/

87

88#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_EXCEPTION\_H\_ \*/

[sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)

#define sys\_define\_gpr\_with\_alias(name1, name2)

**Definition** arch.h:23

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[fatal](test__utils_8h.md#a0c05eeb12526a2c168109f7e5a40d833)

static void fatal(uint32\_t testnum, const void \*expected, size\_t expectedlen, const void \*computed, size\_t computedlen)

**Definition** test\_utils.h:50

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [exception.h](arm_2cortex__a__r_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
