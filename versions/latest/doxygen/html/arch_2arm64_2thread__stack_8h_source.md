---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm64_2thread__stack_8h_source.html
original_path: doxygen/html/arch_2arm64_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h

[Go to the documentation of this file.](arch_2arm64_2thread__stack_8h.md)

1/\*

2 \* Copyright (c) 2020 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_STACK\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_STACK\_H\_

9

10#include <[zephyr/arch/arm64/mm.h](arch_2arm64_2mm_8h.md)>

11

[ 12](arch_2arm64_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

13

14#if defined(CONFIG\_USERSPACE) || defined(CONFIG\_ARM64\_STACK\_PROTECTION)

15#define Z\_ARM64\_STACK\_BASE\_ALIGN MEM\_DOMAIN\_ALIGN\_AND\_SIZE

16#define Z\_ARM64\_STACK\_SIZE\_ALIGN MEM\_DOMAIN\_ALIGN\_AND\_SIZE

17#else

18#define Z\_ARM64\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

19#define Z\_ARM64\_STACK\_SIZE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

20#endif

21

22#if defined(CONFIG\_ARM64\_STACK\_PROTECTION)

23#define Z\_ARM64\_STACK\_GUARD\_SIZE MEM\_DOMAIN\_ALIGN\_AND\_SIZE

24#define Z\_ARM64\_K\_STACK\_BASE\_ALIGN MEM\_DOMAIN\_ALIGN\_AND\_SIZE

25#else

26#define Z\_ARM64\_STACK\_GUARD\_SIZE 0

27#define Z\_ARM64\_K\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

28#endif

29

30/\*

31 \* [ see also comments in arch/arm64/core/thread.c ]

32 \*

33 \* High memory addresses

34 \*

35 \* +-------------------+ <- thread.stack\_info.start + thread.stack\_info.size

36 \* | TLS |

37 \* +-------------------+ <- initial sp (computable with thread.stack\_info.delta)

38 \* | |

39 \* | Used stack |

40 \* | |

41 \* +...................+ <- thread's current stack pointer

42 \* | |

43 \* | Unused stack |

44 \* | |

45 \* +-------------------+ <- thread.stack\_info.start

46 \* | Privileged stack | } K\_(THREAD|KERNEL)\_STACK\_RESERVED

47 \* +-------------------+ <- thread stack limit (update on every context switch)

48 \* | Stack guard | } Z\_ARM64\_STACK\_GUARD\_SIZE (protected by MMU/MPU)

49 \* +-------------------+ <- thread.stack\_obj

50 \*

51 \* Low Memory addresses

52 \*/

53

54/\* thread stack \*/

[ 55](arch_2arm64_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_ARM64\_STACK\_BASE\_ALIGN

[ 56](arch_2arm64_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

57 ROUND\_UP((size), Z\_ARM64\_STACK\_SIZE\_ALIGN)

[ 58](arch_2arm64_2thread__stack_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED CONFIG\_PRIVILEGED\_STACK\_SIZE + \

59 Z\_ARM64\_STACK\_GUARD\_SIZE

60

61/\* kernel stack \*/

[ 62](arch_2arm64_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af)#define ARCH\_KERNEL\_STACK\_RESERVED Z\_ARM64\_STACK\_GUARD\_SIZE

[ 63](arch_2arm64_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6)#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_ARM64\_K\_STACK\_BASE\_ALIGN

64

65#ifndef \_ASMLANGUAGE

66

67struct z\_arm64\_thread\_stack\_header {

68 char privilege\_stack[CONFIG\_PRIVILEGED\_STACK\_SIZE];

69} \_\_packed \_\_aligned(Z\_ARM64\_STACK\_BASE\_ALIGN);

70

71#endif /\* \_ASMLANGUAGE \*/

72

73#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_STACK\_H\_ \*/

[mm.h](arch_2arm64_2mm_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [thread\_stack.h](arch_2arm64_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
