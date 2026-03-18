---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2x86_2thread__stack_8h_source.html
original_path: doxygen/html/arch_2x86_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h

[Go to the documentation of this file.](arch_2x86_2thread__stack_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_THREAD\_STACK\_H

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_THREAD\_STACK\_H

8

9#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h.md)>

10

11#ifdef CONFIG\_X86\_64

12#define ARCH\_STACK\_PTR\_ALIGN 16UL

13#else

[ 14](arch_2x86_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4UL

15#endif

16

17#if defined(CONFIG\_HW\_STACK\_PROTECTION) || defined(CONFIG\_USERSPACE)

18#define Z\_X86\_STACK\_BASE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

19#else

20#define Z\_X86\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

21#endif

22

23#ifdef CONFIG\_USERSPACE

24/\* If user mode enabled, expand any stack size to fill a page since that is

25 \* the access control granularity and we don't want other kernel data to

26 \* unintentionally fall in the latter part of the page

27 \*/

28#define Z\_X86\_STACK\_SIZE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

29#else

30#define Z\_X86\_STACK\_SIZE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

31#endif

32

33#ifndef \_ASMLANGUAGE

34/\* With both hardware stack protection and userspace enabled, stacks are

35 \* arranged as follows:

36 \*

37 \* High memory addresses

38 \* +-----------------------------------------+

39 \* | Thread stack (varies) |

40 \* +-----------------------------------------+

41 \* | Privilege elevation stack |

42 \* | (4096 bytes) |

43 \* +-----------------------------------------+

44 \* | Guard page (4096 bytes) |

45 \* +-----------------------------------------+

46 \* Low Memory addresses

47 \*

48 \* Privilege elevation stacks are fixed-size. All the pages containing the

49 \* thread stack are marked as user-accessible. The guard page is marked

50 \* read-only to catch stack overflows in supervisor mode.

51 \*

52 \* If a thread starts in supervisor mode, the page containing the

53 \* privilege elevation stack is also marked read-only.

54 \*

55 \* If a thread starts in, or drops down to user mode, the privilege stack page

56 \* will be marked as present, supervisor-only.

57 \*

58 \* If KPTI is not enabled, the \_main\_tss.esp0 field will always be updated

59 \* updated to point to the top of the privilege elevation stack. Otherwise

60 \* \_main\_tss.esp0 always points to the trampoline stack, which handles the

61 \* page table switch to the kernel PDPT and transplants context to the

62 \* privileged mode stack.

63 \*/

64struct z\_x86\_thread\_stack\_header {

65#ifdef CONFIG\_HW\_STACK\_PROTECTION

66 char guard\_page[CONFIG\_MMU\_PAGE\_SIZE];

67#endif

68#ifdef CONFIG\_USERSPACE

69 char privilege\_stack[CONFIG\_MMU\_PAGE\_SIZE];

70#endif /\* CONFIG\_USERSPACE \*/

71} \_\_packed \_\_aligned(Z\_X86\_STACK\_BASE\_ALIGN);

72

[ 73](arch_2x86_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_X86\_STACK\_BASE\_ALIGN

74

[ 75](arch_2x86_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

76 ROUND\_UP((size), Z\_X86\_STACK\_SIZE\_ALIGN)

77

[ 78](arch_2x86_2thread__stack_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED \

79 sizeof(struct z\_x86\_thread\_stack\_header)

80

81#ifdef CONFIG\_HW\_STACK\_PROTECTION

82#define ARCH\_KERNEL\_STACK\_RESERVED CONFIG\_MMU\_PAGE\_SIZE

83#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

84#else

[ 85](arch_2x86_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af)#define ARCH\_KERNEL\_STACK\_RESERVED 0

[ 86](arch_2x86_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6)#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_STACK\_PTR\_ALIGN

87#endif

88

89#endif /\* !\_ASMLANGUAGE \*/

90#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_THREAD\_STACK\_H \*/

[mmustructs.h](mmustructs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [thread\_stack.h](arch_2x86_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
