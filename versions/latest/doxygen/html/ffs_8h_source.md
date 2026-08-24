---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ffs_8h_source.html
original_path: doxygen/html/ffs_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ffs.h

[Go to the documentation of this file.](ffs_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \* Copyright (c) 2017, Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

31

[ 32](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op)

33{

34 if (op == 0) {

35 return 0;

36 }

37

38 return 32 - \_\_builtin\_clz(op);

39}

40

41

53

[ 54](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [find\_lsb\_set](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op)

55{

56#ifdef CONFIG\_TOOLCHAIN\_HAS\_BUILTIN\_FFS

57 return \_\_builtin\_ffs(op);

58

59#else

60 /\*

61 \* Toolchain does not have \_\_builtin\_ffs(). Leverage find\_lsb\_set()

62 \* by first clearing all but the lowest set bit.

63 \*/

64

65 op = op ^ (op & (op - 1));

66

67 return [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(op);

68#endif /\* CONFIG\_TOOLCHAIN\_HAS\_BUILTIN\_FFS \*/

69}

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif /\* \_ASMLANGUAGE \*/

76

77#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_ \*/

[find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)

static ALWAYS\_INLINE unsigned int find\_msb\_set(uint32\_t op)

find most significant bit set in a 32-bit word

**Definition** ffs.h:32

[find\_lsb\_set](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)

static ALWAYS\_INLINE unsigned int find\_lsb\_set(uint32\_t op)

find least significant bit set in a 32-bit word

**Definition** ffs.h:54

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [ffs.h](ffs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
