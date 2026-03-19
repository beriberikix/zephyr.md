---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2xtensa_2thread__stack_8h_source.html
original_path: doxygen/html/arch_2xtensa_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

12#include <[zephyr/sys/util.h](sys_2util_8h.md)>

13

14#ifdef CONFIG\_KERNEL\_COHERENCE

15#define ARCH\_STACK\_PTR\_ALIGN XCHAL\_DCACHE\_LINESIZE

16#else

[ 17](arch_2xtensa_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

18#endif

19

20

21#ifdef CONFIG\_USERSPACE

22#ifdef CONFIG\_XTENSA\_MMU

23#define XTENSA\_STACK\_BASE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

24#define XTENSA\_STACK\_SIZE\_ALIGN CONFIG\_MMU\_PAGE\_SIZE

25#endif

26#ifdef CONFIG\_XTENSA\_MPU

27#define XTENSA\_STACK\_BASE\_ALIGN XCHAL\_MPU\_ALIGN

28#define XTENSA\_STACK\_SIZE\_ALIGN XCHAL\_MPU\_ALIGN

29#endif

30#else

31#define XTENSA\_STACK\_BASE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

32#define XTENSA\_STACK\_SIZE\_ALIGN ARCH\_STACK\_PTR\_ALIGN

33#endif

34

35/\*

36 \*

37 \* High memory addresses

38 \*

39 \* +-------------------+ <- thread.stack\_info.start + thread.stack\_info.size

40 \* | TLS |

41 \* +-------------------+ <- initial sp (computable with thread.stack\_info.delta)

42 \* | |

43 \* | Thread stack |

44 \* | |

45 \* +-------------------+ <- thread.stack\_info.start

46 \* | Privileged stack | } CONFIG\_MMU\_PAGE\_SIZE

47 \* +-------------------+ <- thread.stack\_obj

48 \*

49 \* Low Memory addresses

50 \*/

51

52#ifndef \_ASMLANGUAGE

53

54/\* thread stack \*/

[ 55](structxtensa__thread__stack__header.md)struct [xtensa\_thread\_stack\_header](structxtensa__thread__stack__header.md) {

56#if defined(CONFIG\_XTENSA\_MMU) || defined(CONFIG\_XTENSA\_MPU)

57 char privilege\_stack[CONFIG\_PRIVILEGED\_STACK\_SIZE];

58#endif /\* CONFIG\_XTENSA\_MPU \*/

59} \_\_packed \_\_aligned(XTENSA\_STACK\_BASE\_ALIGN);

60

61#if defined(CONFIG\_XTENSA\_MMU) || defined(CONFIG\_XTENSA\_MPU)

62#define ARCH\_THREAD\_STACK\_RESERVED \

63 sizeof(struct xtensa\_thread\_stack\_header)

64#endif /\* CONFIG\_XTENSA\_MMU || CONFIG\_XTENSA\_MPU \*/

65

[ 66](arch_2xtensa_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) XTENSA\_STACK\_BASE\_ALIGN

[ 67](arch_2xtensa_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

68 ROUND\_UP((size), XTENSA\_STACK\_SIZE\_ALIGN)

69

70/\* kernel stack \*/

[ 71](arch_2xtensa_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af)#define ARCH\_KERNEL\_STACK\_RESERVED 0

[ 72](arch_2xtensa_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6)#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_STACK\_PTR\_ALIGN

73

74#endif /\* \_ASMLANGUAGE \*/

75

76#endif

[xtensa\_thread\_stack\_header](structxtensa__thread__stack__header.md)

**Definition** thread\_stack.h:55

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [thread\_stack.h](arch_2xtensa_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
