---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/assert_8h_source.html
original_path: doxygen/html/assert_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

assert.h

[Go to the documentation of this file.](assert_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \* Copyright (c) 2016, Freescale Semiconductor, Inc.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ASSERT\_H\_

9#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ASSERT\_H\_

10

11#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#else

16#if \_\_STDC\_VERSION\_\_ >= 201112L

17#define static\_assert \_Static\_assert

18#endif /\* \_\_STDC\_VERSION\_\_ \*/

19#endif /\* \_\_cplusplus \*/

20

21#ifndef NDEBUG

22#ifndef assert

[ 23](assert_8h.md#ac88d9686b15e03eb62e2a66109845f86)#define assert(test) \_\_ASSERT\_NO\_MSG(test)

24#endif

25#else

26#ifndef assert

27#define assert(test) ((void)0)

28#endif

29#endif

30

31#ifdef \_\_cplusplus

32}

33#endif

34

35#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ASSERT\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [assert.h](assert_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
