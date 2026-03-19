---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ztest_8h_source.html
original_path: doxygen/html/ztest_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest.h

[Go to the documentation of this file.](ztest_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_ZTEST\_H\_

14#define ZEPHYR\_TESTSUITE\_INCLUDE\_ZTEST\_H\_

15

20

21#if !defined(CONFIG\_ZTEST) && !defined(ZTEST\_UNITTEST)

22#error "You need to add CONFIG\_ZTEST to your config file."

23#endif

24

25#ifndef KERNEL

[ 26](ztest_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 8

27/\* FIXME: Properly integrate with Zephyr's arch specific code \*/

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31struct [arch\_esf](structarch__esf.md);

32#ifdef \_\_cplusplus

33}

34#endif

35#endif /\* KERNEL \*/

36

37#include <[zephyr/sys/printk.h](printk_8h.md)>

[ 38](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)#define PRINT printk

39

40#include <[zephyr/kernel.h](kernel_8h.md)>

41

42#include <[zephyr/ztest\_assert.h](ztest__assert_8h.md)>

43#include <[zephyr/ztest\_mock.h](ztest__mock_8h.md)>

44#include <[zephyr/ztest\_test.h](ztest__test_8h.md)>

45#include <[zephyr/tc\_util.h](tc__util_8h.md)>

46

47#ifdef \_\_cplusplus

48extern "C" {

49#endif

50

[ 51](ztest_8h.md#a8a4533f287d99bb2d7c24c0e29c9a449)void [test\_main](ztest_8h.md#a8a4533f287d99bb2d7c24c0e29c9a449)(void);

52

53#ifdef \_\_cplusplus

54}

55#endif

56

57#endif /\* ZEPHYR\_TESTSUITE\_INCLUDE\_ZTEST\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[printk.h](printk_8h.md)

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[tc\_util.h](tc__util_8h.md)

[test\_main](ztest_8h.md#a8a4533f287d99bb2d7c24c0e29c9a449)

void test\_main(void)

[ztest\_assert.h](ztest__assert_8h.md)

Zephyr testing framework assertion macros.

[ztest\_mock.h](ztest__mock_8h.md)

Ztest mocking support.

[ztest\_test.h](ztest__test_8h.md)

Zephyr testing framework \_test.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest.h](ztest_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
