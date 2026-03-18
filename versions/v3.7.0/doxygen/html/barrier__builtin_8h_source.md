---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/barrier__builtin_8h_source.html
original_path: doxygen/html/barrier__builtin_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

barrier\_builtin.h

[Go to the documentation of this file.](barrier__builtin_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_BARRIER\_BUILTIN\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_BARRIER\_BUILTIN\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_SYS\_BARRIER\_H\_

11#error Please include <zephyr/sys/barrier.h>

12#endif

13

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dmem\_fence\_full(void)

21{

22#if defined(\_\_GNUC\_\_)

23 /\* GCC-ism \*/

24 \_\_atomic\_thread\_fence(\_\_ATOMIC\_SEQ\_CST);

25#else

26 atomic\_thread\_fence(memory\_order\_seq\_cst);

27#endif

28}

29

30static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_dsync\_fence\_full(void)

31{

32#if defined(\_\_GNUC\_\_)

33 /\* GCC-ism \*/

34 \_\_atomic\_thread\_fence(\_\_ATOMIC\_SEQ\_CST);

35#else

36 atomic\_thread\_fence(memory\_order\_seq\_cst);

37#endif

38}

39

40static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_barrier\_isync\_fence\_full(void)

41{

42 \_\_asm\_\_ volatile("" : : : "memory");

43}

44

45#ifdef \_\_cplusplus

46}

47#endif

48

49#endif /\* ZEPHYR\_INCLUDE\_SYS\_BARRIER\_BUILTIN\_H\_ \*/

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [barrier\_builtin.h](barrier__builtin_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
