---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2thread__stack_8h_source.html
original_path: doxygen/html/arch_2xtensa_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h

[Go to the documentation of this file.](arch_2xtensa_2thread__stack_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_STACK\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_STACK\_H\_

9

10#include <xtensa/config/core-isa.h>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12

13#ifdef CONFIG\_KERNEL\_COHERENCE

14#define ARCH\_STACK\_PTR\_ALIGN XCHAL\_DCACHE\_LINESIZE

15#else

[ 16](arch_2xtensa_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

17#endif

18

19

20#if CONFIG\_USERSPACE

[ 21](arch_2xtensa_2thread__stack_8h.md#abfd32aa6dffa0ba9a14e925eac1b57ba)#define XTENSA\_STACK\_BASE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

[ 22](arch_2xtensa_2thread__stack_8h.md#afe73e9fabd5171efb0e480ad1035c21c)#define XTENSA\_STACK\_SIZE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

23#else

24#define XTENSA\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

25#define XTENSA\_STACK\_SIZE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

26#endif

27

28/\*

29 \*

30 \* High memory addresses

31 \*

32 \* +-------------------+ <- thread.stack\_info.start + thread.stack\_info.size

33 \* | TLS |

34 \* +-------------------+ <- initial sp (computable with thread.stack\_info.delta)

35 \* | |

36 \* | Thread stack |

37 \* | |

38 \* +-------------------+ <- thread.stack\_info.start

39 \* | Privileged stack | } CONFIG\_MMU\_PAGE\_SIZE

40 \* +-------------------+ <- thread.stack\_obj

41 \*

42 \* Low Memory addresses

43 \*/

44

45#ifndef \_ASMLANGUAGE

46

47/\* thread stack \*/

48#ifdef CONFIG\_XTENSA\_MMU

49struct xtensa\_thread\_stack\_header {

50 char privilege\_stack[CONFIG\_MMU\_PAGE\_SIZE];

51} \_\_packed \_\_aligned([XTENSA\_STACK\_BASE\_ALIGN](arch_2xtensa_2thread__stack_8h.md#abfd32aa6dffa0ba9a14e925eac1b57ba));

52

53#define ARCH\_THREAD\_STACK\_RESERVED \

54 sizeof(struct xtensa\_thread\_stack\_header)

55#endif /\* CONFIG\_XTENSA\_MMU \*/

56

[ 57](arch_2xtensa_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) XTENSA\_STACK\_BASE\_ALIGN

[ 58](arch_2xtensa_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

59 ROUND\_UP((size), XTENSA\_STACK\_SIZE\_ALIGN)

60

61/\* kernel stack \*/

[ 62](arch_2xtensa_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af)#define ARCH\_KERNEL\_STACK\_RESERVED 0

[ 63](arch_2xtensa_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6)#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_STACK\_PTR\_ALIGN

64

65#endif /\* \_ASMLANGUAGE \*/

66

67#endif

[XTENSA\_STACK\_BASE\_ALIGN](arch_2xtensa_2thread__stack_8h.md#abfd32aa6dffa0ba9a14e925eac1b57ba)

#define XTENSA\_STACK\_BASE\_ALIGN

**Definition** thread\_stack.h:21

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [thread\_stack.h](arch_2xtensa_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
