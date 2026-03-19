---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/arm_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

24#include <cmsis\_core.h>

25

26#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A)

27#include <[zephyr/arch/arm/cortex\_a\_r/cpu.h](arm_2cortex__a__r_2cpu_8h.md)>

28#endif

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\* On ARMv7-M and ARMv8-M Mainline CPUs, this function prevents regular

35 \* exceptions (i.e. with interrupt priority lower than or equal to

36 \* \_EXC\_IRQ\_DEFAULT\_PRIO) from interrupting the CPU. NMI, Faults, SVC,

37 \* and Zero Latency IRQs (if supported) may still interrupt the CPU.

38 \*

39 \* On ARMv6-M and ARMv8-M Baseline CPUs, this function reads the value of

40 \* PRIMASK which shows if interrupts are enabled, then disables all interrupts

41 \* except NMI.

42 \*/

43

[ 44](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

45{

46 unsigned int key;

47

48#if defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

49#if CONFIG\_MP\_MAX\_NUM\_CPUS == 1 || defined(CONFIG\_ARMV8\_M\_BASELINE)

50 key = \_\_get\_PRIMASK();

51 \_\_disable\_irq();

52#else

53#error "Cortex-M0 and Cortex-M0+ require SoC specific support for cross core synchronisation."

54#endif

55#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

56 key = \_\_get\_BASEPRI();

57 \_\_set\_BASEPRI\_MAX(\_EXC\_IRQ\_DEFAULT\_PRIO);

58 \_\_ISB();

59#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

60 || defined(CONFIG\_ARMV7\_A)

61 \_\_asm\_\_ volatile(

62 "mrs %0, cpsr;"

63 "and %0, #" [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)([I\_BIT](arm_2cortex__a__r_2cpu_8h.md#aee2152981b17e0fd7752a41c038f42ad)) ";"

64 "cpsid i;"

65 : "=r" (key)

66 :

67 : "memory", "cc");

68#else

69#error Unknown ARM architecture

70#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

71

72 return key;

73}

74

75

76/\* On Cortex-M0/M0+, this enables all interrupts if they were not

77 \* previously disabled.

78 \*/

79

[ 80](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

81{

82#if defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

83 if (key != 0U) {

84 return;

85 }

86 \_\_enable\_irq();

87 \_\_ISB();

88#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

89 \_\_set\_BASEPRI(key);

90 \_\_ISB();

91#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

92 || defined(CONFIG\_ARMV7\_A)

93 if (key != 0U) {

94 return;

95 }

96 \_\_enable\_irq();

97#else

98#error Unknown ARM architecture

99#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

100}

101

[ 102](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

103{

104 /\* This convention works for both PRIMASK and BASEPRI \*/

105 return key == 0U;

106}

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#endif /\* \_ASMLANGUAGE \*/

113

114#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ASM\_INLINE\_GCC\_H\_ \*/

[arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** asm\_inline\_gcc.h:44

[arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** asm\_inline\_gcc.h:80

[arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** asm\_inline\_gcc.h:102

[cpu.h](arm_2cortex__a__r_2cpu_8h.md)

[I\_BIT](arm_2cortex__a__r_2cpu_8h.md#aee2152981b17e0fd7752a41c038f42ad)

#define I\_BIT

**Definition** cpu.h:32

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [asm\_inline\_gcc.h](arm_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
