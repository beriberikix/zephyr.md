---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2arm_2barrier_8h_source.html
original_path: doxygen/html/arch_2arm_2barrier_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

barrier.h

[Go to the documentation of this file.](arch_2arm_2barrier_8h.md)

1

6#ifndef ZEPHYR\_INCLUDE\_BARRIER\_ARM\_H\_

7#define ZEPHYR\_INCLUDE\_BARRIER\_ARM\_H\_

8

9#ifndef ZEPHYR\_INCLUDE\_SYS\_BARRIER\_H\_

10#error Please include <zephyr/sys/barrier.h>

11#endif

12

13#include <cmsis\_core.h>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dmem\_fence\_full(void)

20{

21 \_\_DMB();

22}

23

24static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dsync\_fence\_full(void)

25{

26 \_\_DSB();

27}

28

29static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_isync\_fence\_full(void)

30{

31 \_\_ISB();

32}

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#endif /\* ZEPHYR\_INCLUDE\_BARRIER\_ARM\_H\_ \*/

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [barrier.h](arch_2arm_2barrier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
