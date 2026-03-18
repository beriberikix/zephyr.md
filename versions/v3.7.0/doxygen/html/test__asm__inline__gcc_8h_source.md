---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/test__asm__inline__gcc_8h_source.html
original_path: doxygen/html/test__asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

test\_asm\_inline\_gcc.h

[Go to the documentation of this file.](test__asm__inline__gcc_8h.md)

1/\* GCC specific test inline assembler functions and macros \*/

2

3/\*

4 \* Copyright (c) 2015, Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef \_TEST\_ASM\_INLINE\_GCC\_H

10#define \_TEST\_ASM\_INLINE\_GCC\_H

11

12#include <[zephyr/sys/barrier.h](sys_2barrier_8h.md)>

13

14#if !defined(\_\_GNUC\_\_)

15#error test\_asm\_inline\_gcc.h goes only with GCC

16#endif

17

18#if defined(CONFIG\_X86)

19static inline void timestamp\_serialize(void)

20{

21 \_\_asm\_\_ \_\_volatile\_\_ (/\* serialize \*/

22 "xorl %%eax,%%eax;\n\t"

23 "cpuid;\n\t"

24 :

25 :

26 : "%eax", "%ebx", "%ecx", "%edx");

27}

28#elif defined(CONFIG\_CPU\_CORTEX\_M) || \

29 defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R) || \

30 defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A) || \

31 defined(CONFIG\_CPU\_CORTEX\_A) || \

32 defined(CONFIG\_CPU\_AARCH64\_CORTEX\_R)

33static inline void timestamp\_serialize(void)

34{

35 [barrier\_isync\_fence\_full](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec)();

36}

37#elif defined(CONFIG\_ARC)

38#define timestamp\_serialize()

39#elif defined(CONFIG\_ARCH\_POSIX)

40#define timestamp\_serialize()

41#elif defined(CONFIG\_XTENSA)

42#define timestamp\_serialize()

43#elif defined(CONFIG\_NIOS2)

44#define timestamp\_serialize()

45#elif defined(CONFIG\_RISCV)

46#define timestamp\_serialize()

47#elif defined(CONFIG\_SPARC)

48#define timestamp\_serialize()

49#elif defined(CONFIG\_MIPS)

50#define timestamp\_serialize()

51#else

52#error implementation of timestamp\_serialize() not provided for your CPU target

53#endif

54

55#endif /\* \_TEST\_ASM\_INLINE\_GCC\_H \*/

[barrier\_isync\_fence\_full](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec)

static ALWAYS\_INLINE void barrier\_isync\_fence\_full(void)

Full/sequentially-consistent instruction synchronization barrier.

**Definition** barrier.h:78

[barrier.h](sys_2barrier_8h.md)

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_asm\_inline\_gcc.h](test__asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
