---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h_source.html
original_path: doxygen/html/subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llvm.h

[Go to the documentation of this file.](subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h.md)

1/\*

2 \* Copyright (c) 2025 Google, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_LLVM\_H\_

8#define ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_LLVM\_H\_

9

10#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_H\_

11#error "Please do not include test toolchain-specific headers directly, \

12use <zephyr/test\_toolchain.h> instead"

13#endif

14

15#include <[zephyr/test\_toolchain/gcc.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)>

16

[ 17](subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h.md#af1ec5706645d6b33ee0781b5e1127796)#define TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW "-Winteger-overflow"

18

19#endif

[gcc.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_toolchain](dir_a3f514c982d37cd960af7c452678e28d.md)
- [llvm.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
