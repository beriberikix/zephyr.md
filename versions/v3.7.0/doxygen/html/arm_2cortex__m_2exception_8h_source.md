---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2cortex__m_2exception_8h_source.html
original_path: doxygen/html/arm_2cortex__m_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

101struct [arch\_esf](structarch__esf.md) {

102 struct [\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) {

[ 103](structarch__esf_1_1____basic__sf.md#a18463f520f3fd820ebcf2bb8038f4be3) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a18463f520f3fd820ebcf2bb8038f4be3)([a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673), r0);

[ 104](structarch__esf_1_1____basic__sf.md#a244545d9b25a77d0cee9ed920b0e1569) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a244545d9b25a77d0cee9ed920b0e1569)([a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84), [r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af));

[ 105](structarch__esf_1_1____basic__sf.md#ac70070052c964b722e45cf0fb5d4809f) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#ac70070052c964b722e45cf0fb5d4809f)([a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83), [r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67));

[ 106](structarch__esf_1_1____basic__sf.md#ada5c058e75b0d72f586a38bd0f48c502) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#ada5c058e75b0d72f586a38bd0f48c502)([a4](structarch__esf.md#a2a794aaedfc9c499f5f98a0bb62936ad), [r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b));

[ 107](structarch__esf_1_1____basic__sf.md#a1d7b65b8d50c59ca7785eef8e3065b0e) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a1d7b65b8d50c59ca7785eef8e3065b0e)(ip, [r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229));

[ 108](structarch__esf_1_1____basic__sf.md#a367345e60d1de623f0167b15e9cae020) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a367345e60d1de623f0167b15e9cae020)([lr](structarch__esf.md#ad9047b114956222cd07503fe9339b43d), [r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca));

[ 109](structarch__esf_1_1____basic__sf.md#a428e8725b8d6c97b29a117fd90afe6a6) [sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a428e8725b8d6c97b29a117fd90afe6a6)([pc](structarch__esf.md#a5547d9c022e6c4a6492df49f11f21493), [r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a));

110 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xpsr](structarch__esf_1_1____basic__sf.md#a1371011f09ff1a5143f24dbd31b064a5);

111 } [basic](structarch__esf.md#a0b4a5972bfeab496a9a0cf0ab7821d63);

112#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING)

113 struct \_\_fpu\_sf [fpu](structarch__esf.md#a89304485b8d99aa30facbddf22465170);

114#endif

115#if defined(CONFIG\_EXTRA\_EXCEPTION\_INFO)

116 struct \_\_extra\_esf\_info extra\_info;

117#endif

118};

119

120extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_arm\_coredump\_fault\_sp;

121

122extern void z\_arm\_exc\_exit(void);

123

124#ifdef \_\_cplusplus

125}

126#endif

127

128#endif /\* \_ASMLANGUAGE \*/

129

130#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_EXCEPTION\_H\_ \*/

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

[arch\_esf::\_\_basic\_sf](structarch__esf_1_1____basic__sf.md)

**Definition** exception.h:64

[arch\_esf::\_\_basic\_sf::xpsr](structarch__esf_1_1____basic__sf.md#a1371011f09ff1a5143f24dbd31b064a5)

uint32\_t xpsr

**Definition** exception.h:72

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a18463f520f3fd820ebcf2bb8038f4be3)

sys\_define\_gpr\_with\_alias(a1, r0)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a1d7b65b8d50c59ca7785eef8e3065b0e)

sys\_define\_gpr\_with\_alias(ip, r12)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a244545d9b25a77d0cee9ed920b0e1569)

sys\_define\_gpr\_with\_alias(a2, r1)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a367345e60d1de623f0167b15e9cae020)

sys\_define\_gpr\_with\_alias(lr, r14)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#a428e8725b8d6c97b29a117fd90afe6a6)

sys\_define\_gpr\_with\_alias(pc, r15)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#ac70070052c964b722e45cf0fb5d4809f)

sys\_define\_gpr\_with\_alias(a3, r2)

[arch\_esf::\_\_basic\_sf::sys\_define\_gpr\_with\_alias](structarch__esf_1_1____basic__sf.md#ada5c058e75b0d72f586a38bd0f48c502)

sys\_define\_gpr\_with\_alias(a4, r3)

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:57

[arch\_esf::basic](structarch__esf.md#a0b4a5972bfeab496a9a0cf0ab7821d63)

struct arch\_esf::\_\_basic\_sf basic

[arch\_esf::a4](structarch__esf.md#a2a794aaedfc9c499f5f98a0bb62936ad)

unsigned long a4

**Definition** exception.h:68

[arch\_esf::a3](structarch__esf.md#a3f2e9029daddabeefd2b2c253efd6c83)

unsigned long a3

**Definition** exception.h:38

[arch\_esf::r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67)

uint32\_t r2

**Definition** exception.h:20

[arch\_esf::pc](structarch__esf.md#a5547d9c022e6c4a6492df49f11f21493)

uint32\_t pc

**Definition** exception.h:21

[arch\_esf::r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b)

uint32\_t r3

**Definition** exception.h:21

[arch\_esf::a1](structarch__esf.md#a62a1feb37b8724ada83d70caae38a673)

unsigned long a1

**Definition** exception.h:36

[arch\_esf::r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af)

uint32\_t r1

**Definition** exception.h:19

[arch\_esf::fpu](structarch__esf.md#a89304485b8d99aa30facbddf22465170)

struct \_\_fpu\_sf fpu

**Definition** exception.h:62

[arch\_esf::r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a)

uint32\_t r15

**Definition** exception.h:33

[arch\_esf::r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229)

uint32\_t r12

**Definition** exception.h:30

[arch\_esf::lr](structarch__esf.md#ad9047b114956222cd07503fe9339b43d)

uint64\_t lr

**Definition** exception.h:47

[arch\_esf::a2](structarch__esf.md#adc1040e4224662f77875db24635ceb84)

unsigned long a2

**Definition** exception.h:37

[arch\_esf::r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca)

uint32\_t r14

**Definition** exception.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [exception.h](arm_2cortex__m_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
