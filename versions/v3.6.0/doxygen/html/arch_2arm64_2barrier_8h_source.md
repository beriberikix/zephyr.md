---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm64_2barrier_8h_source.html
original_path: doxygen/html/arch_2arm64_2barrier_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

barrier.h

[Go to the documentation of this file.](arch_2arm64_2barrier_8h.md)

1

6#ifndef ZEPHYR\_INCLUDE\_BARRIER\_ARM64\_H\_

7#define ZEPHYR\_INCLUDE\_BARRIER\_ARM64\_H\_

8

9#ifndef ZEPHYR\_INCLUDE\_SYS\_BARRIER\_H\_

10#error Please include <zephyr/sys/barrier.h>

11#endif

12

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dmem\_fence\_full(void)

20{

21 \_\_asm\_\_ volatile ("dmb sy" ::: "memory");

22}

23

24static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dsync\_fence\_full(void)

25{

26 \_\_asm\_\_ volatile ("dsb sy" ::: "memory");

27}

28

29static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_isync\_fence\_full(void)

30{

31 \_\_asm\_\_ volatile ("isb" ::: "memory");

32}

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#endif /\* ZEPHYR\_INCLUDE\_BARRIER\_ARM64\_H\_ \*/

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [barrier.h](arch_2arm64_2barrier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
