---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ztest__error__hook_8h_source.html
original_path: doxygen/html/ztest__error__hook_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_error\_hook.h

[Go to the documentation of this file.](ztest__error__hook_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZTEST\_FATAL\_HOOK\_H\_

8#define ZEPHYR\_INCLUDE\_ZTEST\_FATAL\_HOOK\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16#if defined(CONFIG\_ZTEST\_FATAL\_HOOK)

27\_\_syscall void ztest\_set\_fault\_valid(bool valid);

28

29/\* @brief A hook after fatal error handler

30 \*

31 \* @details This is a test case hook that can run code from test case, in

32 \* order to deal with some special case when catching the expected fatal

33 \* error.

34 \*

35 \* Usage: Define your own hook function in your test case code, and do what

36 \* you want to do after fatal error handler.

37 \*

38 \* By default, it will do nothing before leaving error handler.

39 \*/

40void ztest\_post\_fatal\_error\_hook(unsigned int reason,

41 const struct [arch\_esf](structarch__esf.md) \*pEsf);

42

43#endif

44

45

46#if defined(CONFIG\_ZTEST\_ASSERT\_HOOK)

57\_\_syscall void ztest\_set\_assert\_valid(bool valid);

58

59/\* @brief A hook after assert fault handler

60 \*

61 \* @details This is a test case hook that can run code from test case, in

62 \* order to deal with some special case when catching the expected assert

63 \* failed.

64 \*

65 \* Usage: Define your own hook function in your test case code, and do what

66 \* you want to do after assert handler.

67 \*

68 \* By default, it will abort the thread which assert failed.

69 \*/

70void ztest\_post\_assert\_fail\_hook(void);

71

72#endif

73

74#ifdef \_\_cplusplus

75}

76#endif

77

78#if defined(CONFIG\_ZTEST\_FATAL\_HOOK) || defined(CONFIG\_ZTEST\_ASSERT\_HOOK)

79#include <zephyr/syscalls/ztest\_error\_hook.h>

80#endif

81

82#endif /\* ZEPHYR\_INCLUDE\_ZTEST\_FATAL\_HOOK\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:57

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_error\_hook.h](ztest__error__hook_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
