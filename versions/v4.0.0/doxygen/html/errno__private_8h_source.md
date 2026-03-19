---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/errno__private_8h_source.html
original_path: doxygen/html/errno__private_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)> /\* For Z\_THREAD\_LOCAL \*/

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17/\* NOTE: located here to avoid include dependency loops between errno.h

18 \* and kernel.h

19 \*/

20

21#ifdef CONFIG\_LIBC\_ERRNO

22#include <[errno.h](errno_8h.md)>

23

24static inline int \*z\_errno(void)

25{

26 return &[errno](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed);

27}

28

29#elif defined(CONFIG\_ERRNO\_IN\_TLS)

30extern Z\_THREAD\_LOCAL int z\_errno\_var;

31

32static inline int \*z\_errno(void)

33{

34 return &z\_errno\_var;

35}

36#else

45\_\_syscall int \*z\_errno(void);

46

47#endif /\* CONFIG\_ERRNO\_IN\_TLS \*/

48

49#ifdef \_\_cplusplus

50}

51#endif

52

53#if !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

54#include <zephyr/syscalls/errno\_private.h>

55#endif /\* CONFIG\_ERRNO\_IN\_TLS \*/

56

57#endif /\* ZEPHYR\_INCLUDE\_SYS\_ERRNO\_PRIVATE\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[errno](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed)

#define errno

**Definition** errno.h:37

[types.h](include_2zephyr_2types_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [errno\_private.h](errno__private_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
