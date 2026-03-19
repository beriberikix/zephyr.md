---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/include_2zephyr_2arch_2arm_2error_8h_source.html
original_path: doxygen/html/include_2zephyr_2arch_2arm_2error_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](include_2zephyr_2arch_2arm_2error_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2023 Arm Limited

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_

18

19#include <[zephyr/arch/arm/syscall.h](arch_2arm_2syscall_8h.md)>

20#include <[zephyr/arch/arm/exception.h](arm_2exception_8h.md)>

21#include <[stdbool.h](stdbool_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27#if defined(CONFIG\_CPU\_CORTEX\_M)

28/\* ARMv6 will hard-fault if SVC is called with interrupts locked. Just

29 \* force them unlocked, the thread is in an undefined state anyway

30 \*

31 \* On ARMv7m we won't get a HardFault, but if interrupts were locked the

32 \* thread will continue executing after the exception and forbid PendSV to

33 \* schedule a new thread until they are unlocked which is not what we want.

34 \* Force them unlocked as well.

35 \*/

36#define ARCH\_EXCEPT(reason\_p) \

37do {\

38 arch\_irq\_unlock(0); \

39 \_\_asm\_\_ volatile( \

40 "mov r0, %[\_reason]\n" \

41 "svc %[id]\n" \

42 :: [\_reason] "r" (reason\_p), [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT) \

43 : "r0", "memory"); \

44} while (false)

45#elif defined(CONFIG\_ARMV7\_R) || defined(CONFIG\_AARCH32\_ARMV8\_R) \

46 || defined(CONFIG\_ARMV7\_A)

47/\*

48 \* In order to support using svc for an exception while running in an

49 \* isr, stack $lr\_svc before calling svc. While exiting the isr,

50 \* z\_check\_stack\_sentinel is called. $lr\_svc contains the return address.

51 \* If the sentinel is wrong, it calls svc to cause an oops. This svc

52 \* call will overwrite $lr\_svc, losing the return address from the

53 \* z\_check\_stack\_sentinel call if it is not stacked before the svc.

54 \*/

55#define ARCH\_EXCEPT(reason\_p) \

56register uint32\_t r0 \_\_asm\_\_("r0") = reason\_p; \

57do { \

58 \_\_asm\_\_ volatile ( \

59 "push {lr}\n\t" \

60 "cpsie i\n\t" \

61 "svc %[id]\n\t" \

62 "pop {lr}\n\t" \

63 : \

64 : "r" (r0), [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT) \

65 : "memory"); \

66} while (false)

67#else

68#error Unknown ARM architecture

69#endif /\* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE \*/

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ERROR\_H\_ \*/

[syscall.h](arch_2arm_2syscall_8h.md)

ARM AArch32 specific syscall header.

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [error.h](include_2zephyr_2arch_2arm_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
