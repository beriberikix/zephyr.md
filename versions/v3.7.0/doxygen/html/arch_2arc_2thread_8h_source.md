---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2arc_2thread_8h_source.html
original_path: doxygen/html/arch_2arc_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2arc_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_THREAD\_H\_

21

22/\*

23 \* Reason a thread has relinquished control.

24 \*/

25#define \_CAUSE\_NONE 0

26#define \_CAUSE\_COOP 1

27#define \_CAUSE\_RIRQ 2

28#define \_CAUSE\_FIRQ 3

29

30#ifndef \_ASMLANGUAGE

31#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

37struct \_callee\_saved {

38 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) sp; /\* r28 \*/

39};

40typedef struct \_callee\_saved \_callee\_saved\_t;

41

42struct \_thread\_arch {

43

44 /\* one of the \_CAUSE\_xxxx definitions above \*/

45 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) relinquish\_cause;

46

47#ifdef CONFIG\_ARC\_STACK\_CHECKING

48 /\* High address of stack region, stack grows downward from this

49 \* location. Usesd for hardware stack checking

50 \*/

51 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) k\_stack\_base;

52 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) k\_stack\_top;

53#ifdef CONFIG\_USERSPACE

54 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) u\_stack\_base;

55 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) u\_stack\_top;

56#endif

57#endif

58

59#ifdef CONFIG\_USERSPACE

60 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) priv\_stack\_start;

61#endif

62};

63

64typedef struct \_thread\_arch \_thread\_arch\_t;

65

66#ifdef \_\_cplusplus

67}

68#endif

69

70#endif /\* \_ASMLANGUAGE \*/

71

72

73#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [thread.h](arch_2arc_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
