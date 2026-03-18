---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/arm_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline\_gcc.h

[Go to the documentation of this file.](arm_2asm__inline__gcc_8h.md)

1/\* ARM AArch32 GCC specific public inline assembler functions and macros \*/

2

3/\*

4 \* Copyright (c) 2015, Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9/\* Either public functions or macros or invoked by public functions \*/

10

11#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_GCC\_H\_

12#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_GCC\_H\_

13

14/\*

15 \* The file must not be included directly

16 \* Include arch/cpu.h instead

17 \*/

18

19#ifndef \_ASMLANGUAGE

20

21#include <[zephyr/toolchain.h](toolchain_8h.md)>

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[zephyr/arch/arm/exception.h](arm_2exception_8h.md)>

24

25#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A)

26#include <[zephyr/arch/arm/cortex\_a\_r/cpu.h](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md)>

27#endif

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33/\* On ARMv7-M and ARMv8-M Mainline CPUs, this function prevents regular

34 \* exceptions (i.e. with interrupt priority lower than or equal to

35 \* \_EXC\_IRQ\_DEFAULT\_PRIO) from interrupting the CPU. NMI, Faults, SVC,

36 \* and Zero Latency IRQs (if supported) may still interrupt the CPU.

37 \*

38 \* On ARMv6-M and ARMv8-M Baseline CPUs, this function reads the value of

39 \* PRIMASK which shows if interrupts are enabled, then disables all interrupts

40 \* except NMI.

41 \*/

42

[ 43](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

44{

45 unsigned int key;

46

47#if defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

48#if CONFIG\_MP\_MAX\_NUM\_CPUS == 1 || defined(CONFIG\_ARMV8\_M\_BASELINE)

49 \_\_asm\_\_ volatile("mrs %0, PRIMASK;"

50 "cpsid i"

51 : "=r" (key)

52 :

53 : "memory");

54#else

55#error "Cortex-M0 and Cortex-M0+ require SoC specific support for cross core synchronisation."

56#endif

57#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

58 unsigned int tmp;

59

60 \_\_asm\_\_ volatile(

61 "mov %1, %2;"

62 "mrs %0, BASEPRI;"

63 "msr BASEPRI\_MAX, %1;"

64 "isb;"

65 : "=r"(key), "=r"(tmp)

66 : "i"(\_EXC\_IRQ\_DEFAULT\_PRIO)

67 : "memory");

68#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

69 || defined(CONFIG\_ARMV7\_A)

70 \_\_asm\_\_ volatile(

71 "mrs %0, cpsr;"

72 "and %0, #" [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)([I\_BIT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aee2152981b17e0fd7752a41c038f42ad)) ";"

73 "cpsid i;"

74 : "=r" (key)

75 :

76 : "memory", "cc");

77#else

78#error Unknown ARM architecture

79#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

80

81 return key;

82}

83

84

85/\* On Cortex-M0/M0+, this enables all interrupts if they were not

86 \* previously disabled.

87 \*/

88

[ 89](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

90{

91#if defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

92 if (key != 0U) {

93 return;

94 }

95 \_\_asm\_\_ volatile(

96 "cpsie i;"

97 "isb"

98 : : : "memory");

99#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

100 \_\_asm\_\_ volatile(

101 "msr BASEPRI, %0;"

102 "isb;"

103 : : "r"(key) : "memory");

104#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

105 || defined(CONFIG\_ARMV7\_A)

106 if (key != 0U) {

107 return;

108 }

109 \_\_asm\_\_ volatile(

110 "cpsie i;"

111 : : : "memory", "cc");

112#else

113#error Unknown ARM architecture

114#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

115}

116

[ 117](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

118{

119 /\* This convention works for both PRIMASK and BASEPRI \*/

120 return key == 0U;

121}

122

123#ifdef \_\_cplusplus

124}

125#endif

126

127#endif /\* \_ASMLANGUAGE \*/

128

129#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_GCC\_H\_ \*/

[arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** asm\_inline\_gcc.h:43

[arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** asm\_inline\_gcc.h:89

[arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** asm\_inline\_gcc.h:117

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[cpu.h](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md)

[I\_BIT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aee2152981b17e0fd7752a41c038f42ad)

#define I\_BIT

**Definition** cpu.h:30

[types.h](include_2zephyr_2types_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [asm\_inline\_gcc.h](arm_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
