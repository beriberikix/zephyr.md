---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2x86_2thread__stack_8h_source.html
original_path: doxygen/html/arch_2x86_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

17#if defined(CONFIG\_X86\_STACK\_PROTECTION) || defined(CONFIG\_USERSPACE) \

18 || defined(CONFIG\_THREAD\_STACK\_MEM\_MAPPED)

19#define Z\_X86\_STACK\_BASE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

20#else

21#define Z\_X86\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

22#endif

23

24#if defined(CONFIG\_USERSPACE) || defined(CONFIG\_THREAD\_STACK\_MEM\_MAPPED)

25/\* If user mode enabled, expand any stack size to fill a page since that is

26 \* the access control granularity and we don't want other kernel data to

27 \* unintentionally fall in the latter part of the page

28 \*

29 \* This is also true when memory mapped stacks are used with since

30 \* access control applies to one page at a time.

31 \*/

32#define Z\_X86\_STACK\_SIZE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

33#else

34#define Z\_X86\_STACK\_SIZE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

35#endif

36

37#ifndef \_ASMLANGUAGE

38/\* With both hardware stack protection and userspace enabled, stacks are

39 \* arranged as follows:

40 \*

41 \* --- Without stack being memory mapped:

42 \* High memory addresses

43 \* +-----------------------------------------+

44 \* | Thread stack (varies) |

45 \* +-----------------------------------------+

46 \* | Privilege elevation stack |

47 \* | (CONFIG\_PRIVILEGED\_STACK\_SIZE) |

48 \* +-----------------------------------------+

49 \* | Guard page (4096 bytes) |

50 \* | - 'guard\_page' in struct |

51 \* | z\_x86\_thread\_stack\_header |

52 \* +-----------------------------------------+

53 \* Low Memory addresses

54 \*

55 \* --- With stack being memory mapped:

56 \* High memory addresses

57 \* +-----------------------------------------+

58 \* | Guard page (empty page) |

59 \* +-----------------------------------------+

60 \* | Thread stack (varies) |

61 \* +-----------------------------------------+

62 \* | Privilege elevation stack |

63 \* | (CONFIG\_PRIVILEGED\_STACK\_SIZE) |

64 \* +-----------------------------------------+

65 \* | Guard page (empty page) |

66 \* +-----------------------------------------+

67 \* Low Memory addresses

68 \*

69 \* Without memory mapped stacks, the guard page is actually allocated

70 \* as part of the stack struct, which takes up physical memory during

71 \* linking.

72 \*

73 \* Privilege elevation stacks are fixed-size. All the pages containing the

74 \* thread stack are marked as user-accessible. The guard page is marked

75 \* read-only to catch stack overflows in supervisor mode.

76 \*

77 \* If a thread starts in supervisor mode, the page containing the

78 \* privilege elevation stack is also marked read-only.

79 \*

80 \* If a thread starts in, or drops down to user mode, the privilege stack page

81 \* will be marked as present, supervisor-only.

82 \*

83 \* If KPTI is not enabled, the \_main\_tss.esp0 field will always be updated

84 \* updated to point to the top of the privilege elevation stack. Otherwise

85 \* \_main\_tss.esp0 always points to the trampoline stack, which handles the

86 \* page table switch to the kernel PDPT and transplants context to the

87 \* privileged mode stack.

88 \*/

89struct z\_x86\_thread\_stack\_header {

90#if defined(CONFIG\_X86\_STACK\_PROTECTION) && !defined(CONFIG\_THREAD\_STACK\_MEM\_MAPPED)

91 char guard\_page[CONFIG\_MMU\_PAGE\_SIZE];

92#endif

93#ifdef CONFIG\_USERSPACE

94 char privilege\_stack[CONFIG\_PRIVILEGED\_STACK\_SIZE];

95#endif /\* CONFIG\_USERSPACE \*/

96} \_\_packed \_\_aligned(Z\_X86\_STACK\_BASE\_ALIGN);

97

[ 98](arch_2x86_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_X86\_STACK\_BASE\_ALIGN

99

[ 100](arch_2x86_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

101 ROUND\_UP((size), Z\_X86\_STACK\_SIZE\_ALIGN)

102

[ 103](arch_2x86_2thread__stack_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED \

104 sizeof(struct z\_x86\_thread\_stack\_header)

105

106#ifdef CONFIG\_X86\_STACK\_PROTECTION

107#define ARCH\_KERNEL\_STACK\_RESERVED CONFIG\_MMU\_PAGE\_SIZE

108#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

109#else

[ 110](arch_2x86_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af)#define ARCH\_KERNEL\_STACK\_RESERVED 0

[ 111](arch_2x86_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6)#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_STACK\_PTR\_ALIGN

112#endif

113

114#endif /\* !\_ASMLANGUAGE \*/

115#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_THREAD\_STACK\_H \*/

[mmustructs.h](mmustructs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [thread\_stack.h](arch_2x86_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
