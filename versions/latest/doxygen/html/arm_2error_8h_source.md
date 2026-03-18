---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm_2error_8h_source.html
original_path: doxygen/html/arm_2error_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](arm_2error_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_

17

18#include <[zephyr/arch/arm/syscall.h](arch_2arm_2syscall_8h.md)>

19#include <[zephyr/arch/arm/exception.h](arm_2exception_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26#if defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

27/\* ARMv6 will hard-fault if SVC is called with interrupts locked. Just

28 \* force them unlocked, the thread is in an undefined state anyway

29 \*

30 \* On ARMv7m we won't get a HardFault, but if interrupts were locked the

31 \* thread will continue executing after the exception and forbid PendSV to

32 \* schedule a new thread until they are unlocked which is not what we want.

33 \* Force them unlocked as well.

34 \*/

35#define ARCH\_EXCEPT(reason\_p) \

36register uint32\_t r0 \_\_asm\_\_("r0") = reason\_p; \

37do { \

38 \_\_asm\_\_ volatile ( \

39 "cpsie i\n\t" \

40 "svc %[id]\n\t" \

41 : \

42 : "r" (r0), [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT) \

43 : "memory"); \

44} while (false)

45#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

46#define ARCH\_EXCEPT(reason\_p) do { \

47 \_\_asm\_\_ volatile ( \

48 "eors.n r0, r0\n\t" \

49 "msr BASEPRI, r0\n\t" \

50 "mov r0, %[reason]\n\t" \

51 "svc %[id]\n\t" \

52 : \

53 : [reason] "i" (reason\_p), [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT) \

54 : "memory"); \

55} while (false)

56#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

57 || defined(CONFIG\_ARMV7\_A)

58/\*

59 \* In order to support using svc for an exception while running in an

60 \* isr, stack $lr\_svc before calling svc. While exiting the isr,

61 \* z\_check\_stack\_sentinel is called. $lr\_svc contains the return address.

62 \* If the sentinel is wrong, it calls svc to cause an oops. This svc

63 \* call will overwrite $lr\_svc, losing the return address from the

64 \* z\_check\_stack\_sentinel call if it is not stacked before the svc.

65 \*/

66#define ARCH\_EXCEPT(reason\_p) \

67register uint32\_t r0 \_\_asm\_\_("r0") = reason\_p; \

68do { \

69 \_\_asm\_\_ volatile ( \

70 "push {lr}\n\t" \

71 "cpsie i\n\t" \

72 "svc %[id]\n\t" \

73 "pop {lr}\n\t" \

74 : \

75 : "r" (r0), [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT) \

76 : "memory"); \

77} while (false)

78#else

79#error Unknown ARM architecture

80#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

81

82#ifdef \_\_cplusplus

83}

84#endif

85

86#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_ \*/

[syscall.h](arch_2arm_2syscall_8h.md)

ARM AArch32 specific syscall header.

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [error.h](arm_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
