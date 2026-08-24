---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/test__toolchain_8h_source.html
original_path: doxygen/html/test__toolchain_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

test\_toolchain.h

[Go to the documentation of this file.](test__toolchain_8h.md)

1/\*

2 \* Copyright (c) 2025 Google, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_H\_

8#define ZEPHYR\_TESTSUITE\_INCLUDE\_TEST\_TOOLCHAIN\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11

12#if defined(\_\_llvm\_\_) || (defined(\_LINKER) && defined(\_\_LLD\_LINKER\_CMD\_\_))

13#include <[zephyr/test\_toolchain/llvm.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h.md)>

14#elif defined(\_\_GNUC\_\_) || (defined(\_LINKER) && defined(\_\_GCC\_LINKER\_CMD\_\_))

15#include <[zephyr/test\_toolchain/gcc.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)>

16#endif

17

25#ifndef TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN

[ 26](test__toolchain_8h.md#a46a35ee1419f878aff6c4502a82fdad4)#define TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN

27#endif

28

36#ifndef TOOLCHAIN\_WARNING\_DANGLING\_POINTER

[ 37](test__toolchain_8h.md#a41da25e145e8172cebcbbf31e0b79e17)#define TOOLCHAIN\_WARNING\_DANGLING\_POINTER

38#endif

39

47#ifndef TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION

[ 48](test__toolchain_8h.md#ad3a914654f83a6490de9a84d090af496)#define TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION

49#endif

50

58#ifndef TOOLCHAIN\_WARNING\_INFINITE\_RECURSION

[ 59](test__toolchain_8h.md#a01fd2ae9418bafbedeaa4f3aeea9b3a3)#define TOOLCHAIN\_WARNING\_INFINITE\_RECURSION

60#endif

61

69#ifndef TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW

[ 70](test__toolchain_8h.md#af1ec5706645d6b33ee0781b5e1127796)#define TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW

71#endif

72

80#ifndef TOOLCHAIN\_WARNING\_OVERFLOW

[ 81](test__toolchain_8h.md#a4c9cbe2de87a179f951f6d10d0d919fd)#define TOOLCHAIN\_WARNING\_OVERFLOW

82#endif

83

91#ifndef TOOLCHAIN\_WARNING\_PRAGMAS

[ 92](test__toolchain_8h.md#a78adf404c8b66e41066126c0221bd334)#define TOOLCHAIN\_WARNING\_PRAGMAS

93#endif

94

102#ifndef TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY

[ 103](test__toolchain_8h.md#a056ed97bac0f04be423885dc21b9df00)#define TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY

104#endif

105

113#ifndef TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW

[ 114](test__toolchain_8h.md#ac45e9e7740ee6c5e20e0ec813499dad5)#define TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW

115#endif

116

124#ifndef TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION

[ 125](test__toolchain_8h.md#a83c3c63db289d6024c809840492bce08)#define TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION

126#endif

127

135#ifndef TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION

[ 136](test__toolchain_8h.md#af90e0047b2708d02d3f69cd019a584df)#define TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION

137#endif

138

139#endif

[gcc.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2gcc_8h.md)

[llvm.h](subsys_2testsuite_2include_2zephyr_2test__toolchain_2llvm_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_toolchain.h](test__toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
