---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h_source.html
original_path: doxygen/html/subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcc.h

[Go to the documentation of this file.](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)

1/\*

2 \* Copyright (c) 2025 Google, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_GCC\_H\_

8#define ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_GCC\_H\_

9

10#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_H\_

11#error "Please do not include test toolchain-specific headers directly, \

12use <zephyr/test\_toolchain.h> instead"

13#endif

14

[ 15](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#a41da25e145e8172cebcbbf31e0b79e17)#define TOOLCHAIN\_WARNING\_DANGLING\_POINTER "-Wdangling-pointer"

[ 16](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#ad3a914654f83a6490de9a84d090af496)#define TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION "-Wformat-truncation"

[ 17](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#a01fd2ae9418bafbedeaa4f3aeea9b3a3)#define TOOLCHAIN\_WARNING\_INFINITE\_RECURSION "-Winfinite-recursion"

[ 18](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#a4c9cbe2de87a179f951f6d10d0d919fd)#define TOOLCHAIN\_WARNING\_OVERFLOW "-Woverflow"

[ 19](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#a78adf404c8b66e41066126c0221bd334)#define TOOLCHAIN\_WARNING\_PRAGMAS "-Wpragmas"

[ 20](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md#af90e0047b2708d02d3f69cd019a584df)#define TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION "-Wunused-function"

21

22/\* GCC-specific warnings that aren't in clang. \*/

23#if defined(\_\_GNUC\_\_) && !defined(\_\_clang\_\_)

24#define TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN "-Walloc-size-larger-than="

25#define TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW "-Wstringop-overflow"

26#define TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION "-Wstringop-truncation"

27#endif

28

29#endif

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_toolchain](dir_a3f514c982d37cd960af7c452678e28d.md)
- [gcc.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
