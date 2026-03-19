---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ilog2_8h_source.html
original_path: doxygen/html/ilog2_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ilog2.h

[Go to the documentation of this file.](ilog2_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MATH\_ILOG2\_H\_

8#define ZEPHYR\_INCLUDE\_MATH\_ILOG2\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

14#include <[zephyr/sys/util.h](sys_2util_8h.md)>

15

20

[ 39](ilog2_8h.md#a5868c58205e07f1809d0521bf98798c7)#define ilog2\_compile\_time\_const\_u32(n) \

40 ( \

41 ((n) < 2) ? 0 : \

42 (((n) & BIT(31)) == BIT(31)) ? 31 : \

43 (((n) & BIT(30)) == BIT(30)) ? 30 : \

44 (((n) & BIT(29)) == BIT(29)) ? 29 : \

45 (((n) & BIT(28)) == BIT(28)) ? 28 : \

46 (((n) & BIT(27)) == BIT(27)) ? 27 : \

47 (((n) & BIT(26)) == BIT(26)) ? 26 : \

48 (((n) & BIT(25)) == BIT(25)) ? 25 : \

49 (((n) & BIT(24)) == BIT(24)) ? 24 : \

50 (((n) & BIT(23)) == BIT(23)) ? 23 : \

51 (((n) & BIT(22)) == BIT(22)) ? 22 : \

52 (((n) & BIT(21)) == BIT(21)) ? 21 : \

53 (((n) & BIT(20)) == BIT(20)) ? 20 : \

54 (((n) & BIT(19)) == BIT(19)) ? 19 : \

55 (((n) & BIT(18)) == BIT(18)) ? 18 : \

56 (((n) & BIT(17)) == BIT(17)) ? 17 : \

57 (((n) & BIT(16)) == BIT(16)) ? 16 : \

58 (((n) & BIT(15)) == BIT(15)) ? 15 : \

59 (((n) & BIT(14)) == BIT(14)) ? 14 : \

60 (((n) & BIT(13)) == BIT(13)) ? 13 : \

61 (((n) & BIT(12)) == BIT(12)) ? 12 : \

62 (((n) & BIT(11)) == BIT(11)) ? 11 : \

63 (((n) & BIT(10)) == BIT(10)) ? 10 : \

64 (((n) & BIT(9)) == BIT(9)) ? 9 : \

65 (((n) & BIT(8)) == BIT(8)) ? 8 : \

66 (((n) & BIT(7)) == BIT(7)) ? 7 : \

67 (((n) & BIT(6)) == BIT(6)) ? 6 : \

68 (((n) & BIT(5)) == BIT(5)) ? 5 : \

69 (((n) & BIT(4)) == BIT(4)) ? 4 : \

70 (((n) & BIT(3)) == BIT(3)) ? 3 : \

71 (((n) & BIT(2)) == BIT(2)) ? 2 : \

72 1 \

73 )

74

87/\*

88 \* This is in #define form as this needs to also work on

89 \* compile time constants. Doing this as a static inline

90 \* function will result in compiler complaining with

91 \* "initializer element is not constant".

92 \*/

[ 93](ilog2_8h.md#a2696c6303d4c53b65a3a7f7ff771d5eb)#define ilog2(n) \

94 ( \

95 \_\_builtin\_constant\_p(n) ? \

96 ilog2\_compile\_time\_const\_u32(n) : \

97 find\_msb\_set(n) - 1 \

98 )

99

100#endif /\* ZEPHYR\_INCLUDE\_MATH\_ILOG2\_H\_ \*/

[ffs.h](ffs_8h.md)

[stdint.h](stdint_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [math](dir_76cc2d861a01f89f8d0ad119e28af149.md)
- [ilog2.h](ilog2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
