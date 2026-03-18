---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/riscv_2exception_8h_source.html
original_path: doxygen/html/riscv_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](riscv_2exception_8h.md)

1/\*

2 \* Copyright (c) 2016 Jean-Paul Etienne <fractalclone@gmail.com>

3 \* Copyright (c) 2018 Foundries.io Ltd

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_

17

18#ifndef \_ASMLANGUAGE

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/toolchain.h](toolchain_8h.md)>

21

22#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

23#include <soc\_context.h>

24#endif

25

26#ifdef CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING

27#include <soc\_isr\_stacking.h>

28#endif

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\*

35 \* The name of the structure which contains soc-specific state, if

36 \* any, as well as the soc\_esf\_t typedef below, are part of the RISC-V

37 \* arch API.

38 \*

39 \* The contents of the struct are provided by a SOC-specific

40 \* definition in soc\_context.h.

41 \*/

42#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

43struct soc\_esf {

44 SOC\_ESF\_MEMBERS;

45};

46#endif

47

48#if defined(CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING)

49 SOC\_ISR\_STACKING\_ESF\_DECLARE;

50#else

51struct \_\_esf {

52 unsigned long ra; /\* return address \*/

53

54 unsigned long t0; /\* Caller-saved temporary register \*/

55 unsigned long t1; /\* Caller-saved temporary register \*/

56 unsigned long t2; /\* Caller-saved temporary register \*/

57#if !defined(CONFIG\_RISCV\_ISA\_RV32E)

58 unsigned long t3; /\* Caller-saved temporary register \*/

59 unsigned long t4; /\* Caller-saved temporary register \*/

60 unsigned long t5; /\* Caller-saved temporary register \*/

61 unsigned long t6; /\* Caller-saved temporary register \*/

62#endif /\* !CONFIG\_RISCV\_ISA\_RV32E \*/

63

64 unsigned long a0; /\* function argument/return value \*/

65 unsigned long a1; /\* function argument \*/

66 unsigned long a2; /\* function argument \*/

67 unsigned long a3; /\* function argument \*/

68 unsigned long a4; /\* function argument \*/

69 unsigned long a5; /\* function argument \*/

70#if !defined(CONFIG\_RISCV\_ISA\_RV32E)

71 unsigned long a6; /\* function argument \*/

72 unsigned long a7; /\* function argument \*/

73#endif /\* !CONFIG\_RISCV\_ISA\_RV32E \*/

74

75 unsigned long mepc; /\* machine exception program counter \*/

76 unsigned long mstatus; /\* machine status register \*/

77

78 unsigned long s0; /\* callee-saved s0 \*/

79

80#ifdef CONFIG\_USERSPACE

81 unsigned long sp; /\* preserved (user or kernel) stack pointer \*/

82#endif

83

84#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

85 struct soc\_esf soc\_context;

86#endif

87} \_\_aligned(16);

88#endif /\* CONFIG\_RISCV\_SOC\_HAS\_ISR\_STACKING \*/

89

90typedef struct \_\_esf z\_arch\_esf\_t;

91#ifdef CONFIG\_RISCV\_SOC\_CONTEXT\_SAVE

92typedef struct soc\_esf soc\_esf\_t;

93#endif

94

95#ifdef \_\_cplusplus

96}

97#endif

98

99#endif /\* \_ASMLANGUAGE \*/

100

101#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [exception.h](riscv_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
