---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2cortex__m_2exception_8h_source.html
original_path: doxygen/html/arm_2cortex__m_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm_2cortex__m_2exception_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_EXCEPTION\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_EXCEPTION\_H\_

14

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16

17#include <[zephyr/arch/arm/cortex\_m/nvic.h](nvic_8h.md)>

18

19/\* for assembler, only works with constants \*/

20#define Z\_EXC\_PRIO(pri) (((pri) << (8 - NUM\_IRQ\_PRIO\_BITS)) & 0xff)

21

22/\*

23 \* In architecture variants with non-programmable fault exceptions

24 \* (e.g. Cortex-M Baseline variants), hardware ensures processor faults

25 \* are given the highest interrupt priority level. SVCalls are assigned

26 \* the highest configurable priority level (level 0); note, however, that

27 \* this interrupt level may be shared with HW interrupts.

28 \*

29 \* In Cortex variants with programmable fault exception priorities we

30 \* assign the highest interrupt priority level (level 0) to processor faults

31 \* with configurable priority.

32 \* The highest priority level may be shared with either Zero-Latency IRQs (if

33 \* support for the feature is enabled) or with SVCall priority level.

34 \* Regular HW IRQs are always assigned priority levels lower than the priority

35 \* levels for SVCalls, Zero-Latency IRQs and processor faults.

36 \*

37 \* PendSV IRQ (which is used in Cortex-M variants to implement thread

38 \* context-switching) is assigned the lowest IRQ priority level.

39 \*/

40#if defined(CONFIG\_CPU\_CORTEX\_M\_HAS\_PROGRAMMABLE\_FAULT\_PRIOS)

41#define \_EXCEPTION\_RESERVED\_PRIO 1

42#else

43#define \_EXCEPTION\_RESERVED\_PRIO 0

44#endif

45

46#define \_EXC\_FAULT\_PRIO 0

47#define \_EXC\_ZERO\_LATENCY\_IRQS\_PRIO 0

48#define \_EXC\_SVC\_PRIO COND\_CODE\_1(CONFIG\_ZERO\_LATENCY\_IRQS, \

49 (CONFIG\_ZERO\_LATENCY\_LEVELS), (0))

50#define \_IRQ\_PRIO\_OFFSET (\_EXCEPTION\_RESERVED\_PRIO + \_EXC\_SVC\_PRIO)

[ 51](arm_2cortex__m_2exception_8h.md#a4c24fa1a72ad3c5d08ba7dc48b7d6bd9)#define IRQ\_PRIO\_LOWEST (BIT(NUM\_IRQ\_PRIO\_BITS) - (\_IRQ\_PRIO\_OFFSET) - 1)

52

53#define \_EXC\_IRQ\_DEFAULT\_PRIO Z\_EXC\_PRIO(\_IRQ\_PRIO\_OFFSET)

54

55/\* Use lowest possible priority level for PendSV \*/

56#define \_EXC\_PENDSV\_PRIO 0xff

57#define \_EXC\_PENDSV\_PRIO\_MASK Z\_EXC\_PRIO(\_EXC\_PENDSV\_PRIO)

58

59#ifdef \_ASMLANGUAGE

60GTEXT(z\_arm\_exc\_exit);

61#else

62#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

63

64#ifdef \_\_cplusplus

65extern "C" {

66#endif

67

68#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

69

70/\* Registers s16-s31 (d8-d15, q4-q7) must be preserved across subroutine calls.

71 \*

72 \* Registers s0-s15 (d0-d7, q0-q3) do not have to be preserved (and can be used

73 \* for passing arguments or returning results in standard procedure-call variants).

74 \*

75 \* Registers d16-d31 (q8-q15), do not have to be preserved.

76 \*/

77struct \_\_fpu\_sf {

78 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[16]; /\* s0~s15 (d0-d7) \*/

79#ifdef CONFIG\_VFP\_FEATURE\_REGS\_S64\_D32

80 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)[16]; /\* d16~d31 \*/

81#endif

82 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpscr;

83 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) undefined;

84};

85#endif

86

87/\* Additional register state that is not stacked by hardware on exception

88 \* entry.

89 \*

90 \* These fields are ONLY valid in the ESF copy passed into z\_arm\_fatal\_error().

91 \* When information for a member is unavailable, the field is set to zero.

92 \*/

93#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

94struct \_\_extra\_esf\_info {

95 \_callee\_saved\_t \*callee;

96 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) msp;

97 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) exc\_return;

98};

99#endif /\* CONFIG\_EXTRA\_EXCEPTION\_INFO \*/

100

101struct \_\_esf {

102 struct \_\_basic\_sf {

103 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a1, r0);

104 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a2, r1);

105 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a3, r2);

106 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(a4, r3);

107 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(ip, r12);

108 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(lr, r14);

109 [sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)(pc, r15);

110 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xpsr;

111 } basic;

112#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

113 struct \_\_fpu\_sf fpu;

114#endif

115#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

116 struct \_\_extra\_esf\_info extra\_info;

117#endif

118};

119

120extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arm\_coredump\_fault\_sp;

121

122typedef struct \_\_esf z\_arch\_esf\_t;

123

124extern void z\_arm\_exc\_exit(void);

125

126#ifdef \_\_cplusplus

127}

128#endif

129

130#endif /\* \_ASMLANGUAGE \*/

131

132#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_EXCEPTION\_H\_ \*/

[sys\_define\_gpr\_with\_alias](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)

#define sys\_define\_gpr\_with\_alias(name1, name2)

**Definition** arch.h:23

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[types.h](include_2zephyr_2types_8h.md)

[nvic.h](nvic_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [exception.h](arm_2cortex__m_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
