---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/errno__private_8h_source.html
original_path: doxygen/html/errno__private_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

errno\_private.h

[Go to the documentation of this file.](errno__private_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_ERRNO\_PRIVATE\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_ERRNO\_PRIVATE\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16/\* NOTE: located here to avoid include dependency loops between errno.h

17 \* and kernel.h

18 \*/

19

20#ifdef CONFIG\_LIBC\_ERRNO

21#include <[errno.h](errno_8h.md)>

22

23static inline int \*z\_errno(void)

24{

25 return &[errno](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed);

26}

27

28#elif defined(CONFIG\_ERRNO\_IN\_TLS)

29extern \_\_thread int z\_errno\_var;

30

31static inline int \*z\_errno(void)

32{

33 return &z\_errno\_var;

34}

35#else

44\_\_syscall int \*z\_errno(void);

45

46#endif /\* CONFIG\_ERRNO\_IN\_TLS \*/

47

48#ifdef \_\_cplusplus

49}

50#endif

51

52#if !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

53#include <zephyr/syscalls/errno\_private.h>

54#endif /\* CONFIG\_ERRNO\_IN\_TLS \*/

55

56#endif /\* ZEPHYR\_INCLUDE\_SYS\_ERRNO\_PRIVATE\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[errno](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed)

#define errno

**Definition** errno.h:37

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [errno\_private.h](errno__private_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
